CREATE TABLE `taxi`.`jobmas` ( `JOBID` VARCHAR(20) NOT NULL ,  `Status` VARCHAR(5) NOT NULL ,  `Comefrom` VARCHAR(10) NOT NULL ,  `JOBTIME` TIMESTAMP(6) NOT NULL ,    PRIMARY KEY  (`JOBID`(20))) ENGINE = InnoDB;
INSERT INTO jobmas VALUES('A002','Done','APP','2018-09-13 20:15:09.122');
INSERT INTO jobmas VALUES('A003','Cancel','APP','2018-09-13 06:15:09.122');
INSERT INTO jobmas VALUES('A004','Cancel','AGC2','2018-09-14 15:02:59.123');
INSERT INTO jobmas VALUES('A005','Done','AGC1','2018-09-22 01:52:40.124');
INSERT INTO jobmas VALUES('A006','Done','APP','2018-09-28 09:38:19.125');


CREATE TABLE `taxi`.`jobadd` ( `JOBID` VARCHAR(10) NOT NULL ,  `CITY` TEXT NOT NULL ,  `CARID` VARCHAR(10) NOT NULL ,    PRIMARY KEY  (`JOBID`(10))) ENGINE = InnoDB;
INSERT INTO jobadd VALUES('A001','台北市','12356');
INSERT INTO jobadd VALUES('A002','台中市','225');
INSERT INTO jobadd VALUES('A003','台中市','38654');
INSERT INTO jobadd VALUES('A004','台北市','6654');
INSERT INTO jobadd VALUES('A005','高雄市','7725');
INSERT INTO jobadd VALUES('A006','台北市','801');
INSERT INTO jobadd VALUES('A007','台北市','5586');

CREATE TABLE `taxi`.`JOBPAY` ( `JOBID` VARCHAR(10) NOT NULL ,  `paytype` VARCHAR(10)  ,  `FinialFare` VARCHAR(10)  ,    PRIMARY KEY  (`JOBID`(10))) ENGINE = InnoDB;
INSERT INTO jobadd VALUES('A001',1,100);
INSERT INTO jobadd VALUES('A002',2,80);
INSERT INTO jobadd VALUES('A003',NULL,NULL);
INSERT INTO jobadd VALUES('A004',NULL,NULL);
INSERT INTO jobadd VALUES('A005',1,255);
INSERT INTO jobadd VALUES('A006',2,125);
INSERT INTO jobadd VALUES('A007',2,300);

第一題正解
SELECT CASE 
    WHEN jobpay.paytype = 2 THEN 'paytype2 '
    WHEN jobpay.paytype = 1 THEN 'paytype1 ' 
        END AS paytype_name ,COUNT(jobpay.paytype) as paycount 
    FROM jobmas,jobpay 
    WHERE jobmas.Status = 'Done' AND jobpay.paytype <> '' AND jobpay.JOBID = jobmas.JOBID 
    GROUP BY jobpay.CITY


第二題

--Original = 原始任務數--
SELECT COUNT(a.Status) AS Orignal,COUNT(b.Status)AS Done,COUNT(c.Status)AS AGC_Done 
    FROM    (SELECT* FROM jobmas m WHERE m.JOBTIME BETWEEN '2018-09-01 08:%' AND '2018-09-28 09:%')AS a 
        LEFT OUTER JOIN 
            (SELECT* FROM jobmas m WHERE m.Status = 'Done' AND m.JOBTIME BETWEEN '2018-09-01 08:%' AND '2018-09-28 09:%') AS b ON a.JOBID = b.JOBID 
        LEFT OUTER JOIN 
            (SELECT* FROM jobmas m WHERE m.Status = 'Done' AND m.Comefrom<> 'APP'AND m.JOBTIME BETWEEN '2018-09-01 08:%' AND '2018-09-28 09:%') AS c ON a.JOBID =c.JOBID

