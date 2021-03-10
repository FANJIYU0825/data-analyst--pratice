#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Utilities for creating the ML dataset from experience records."""
import os
import time
import json
import logging
import datetime
import numpy as np
from tqdm import tqdm
from scipy import stats
import matplotlib.pyplot as plt
from src.util import ddb_util, LOGGER, date_util, py_util


def acc(e):
    aa = [x for x in e['experience'] if x['x'] == 'A']
    n = len(aa)
    num_wrong = sum(1 for x in aa if 'm' in x.keys())
    return (n - num_wrong) / float(n)


def get_data(use_cache=True, date=None):
    LOGGER.setLevel(logging.CRITICAL)
    ddb = ddb_util.LambdaDDB('cnprod')

    if date is None:
        date = date_util.date_to_str(datetime.date.today())
    raw_file_name = 'tmp/ml_exp_%s_raw.json' % date
    file_name = 'tmp/ml_exp_%s.json' % date

    if not use_cache or not os.path.exists(raw_file_name):
        print('Scanning experience table - this is going to take a while...')
        start = time.time()
        experience = ddb.scan(table_name='experience')
        print('Scan complete! It took %ssecs.' % (time.time() - start))
        with open(raw_file_name, 'w') as f:
            f.write(json.dumps(experience, cls=py_util.DecimalEncoder))
    else:
        print('Using cached data...')
        with open(raw_file_name) as f:
            experience = json.loads(f.read())

    if not os.path.exists(file_name):
        print('Augmenting data...')
        print('Scanning students...')
        students = ddb.scan(table_name='students')
        junk = []
        with tqdm(total=len(experience)) as pbar:
            for e in experience:
                student = next((s for s in students
                                if s['student_pin'] == e['usr']),
                               None)
                if student is None:
                    junk.append(e)
                    pbar.update()
                    continue

                e['class'] = student['class_code']
                e['teacher'] = student['teacher']
                e['school'] = student['schoolName']
                e['school_group'] = student['schoolGroupName']

                if e['school_group'] not in ['Xian', '瑞兴艺术幼儿园']:
                    junk.append(e)
                    pbar.update()
                    continue

                e['level'] = e['cls_loc'].split('_')[1][0]
                e['unit_module'] = e['cls_loc'].split('_')[1][1:]
                e.pop('cls_loc')

                e['duration'] = e['dur']
                e.pop('dur')

                e['experience'] = e['exp']
                e.pop('exp')

                e['scoring_model'] = e['mod']
                e.pop('mod')

                e['is_preview'] = e['pre']
                e.pop('pre')

                e['score'] = e['scr']
                e.pop('scr')

                e['user'] = e['usr']
                e.pop('usr')

                e['timestamp'] = e['date']
                e.pop('date')

                if 'A' in [x['x'] for x in e['experience']]:
                    e['accuracy'] = acc(e)

                pbar.update()
        print('Removing junk...')
        with tqdm(total=len(junk)) as pbar:
            for j in junk:
                experience.remove(j)
                pbar.update()
        with open(file_name, 'w') as f:
            print('Writing adapted data back to json...')
            f.write(json.dumps(experience, cls=py_util.DecimalEncoder))
    else:
        with open(file_name) as f:
            experience = json.loads(f.read())

    return experience


def score_vs_acc(X, title=''):
    X = list(sorted(X, key=lambda x: x['score']))
    scores = [x['score'] for x in X]
    accs = [x['accuracy'] for x in X]
    corr, p = stats.pearsonr(scores, accs)

    print('Basic stats:')
    print('\tPearson Correlation: %s (%s)' % (corr, p))
    print('\tScores:')
    print('\t\tMean: %s' % np.mean(scores))
    print('\t\tStd: %s' % np.std(scores))
    print('\tAccuracies:')
    print('\t\tMean: %s' % np.mean(accs))
    print('\t\tStd: %s' % np.std(accs))

    plt.figure(figsize=(8, 8))
    plt.scatter(scores, accs)
    plt.xlabel('score')
    plt.ylabel('accuracy')
    plt.title('Correlation of score with accuracy%s'
              % (' (%s)' % title if title else ''))
    plt.show()
