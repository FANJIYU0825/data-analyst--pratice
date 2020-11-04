%% Generate document with:
%% bibtex la_600 && latex -src-specials la_600
%
%\NeedsTeXFormat{LaTeX2e}[1994/12/01]
\documentclass[twoside,openright]{book}

%% Charset & Font:
\usepackage{CJKutf8}

\usepackage{amsmath,amsfonts,amssymb,amsbsy}
\usepackage{amsthm}
%\usepackage{graphpap,ifthen}
%\usepackage{natbib}
%\usepackage{titlesec,titletoc}
\usepackage{mathptmx}

%\usepackage[dvipdfm]{hyperref}
%\usepackage[dvipdfm]{graphicx}
\usepackage{color}

%\usepackage{fancybox}
%\usepackage{fancyhdr}
%\usepackage{texshade}
%\setcounter{tocdepth}{2}
%\usepackage[letterpaper,pdftex=true]{geometry}

%\pagestyle{myheadings}
%\markboth{EchoWin Technologies Inc.}{}

\input{../../include/thmenv_c}
\input{../../include/usrdef}

\renewcommand{\baselinestretch}{1}
%\setlength{\parindent}{2em}
%\pagenumbering{roman}
%\pagenumbering{arabic}

%\newlength{\templength}
%\setlength{\templength}{\oddsidemargin}
%\setlength{\oddsidemargin}{\evensidemargin}
%\setlength{\evensidemargin}{\templength}

\begin{document}
\begin{CJK*}{UTF8}{}
\CJKtilde
\CJKfamily{gbsn}

\renewcommand{\bibname}{参考文献}

\frontmatter

\title{\Huge{\textbf{LECTURE NOTES}} \\ \Huge{\textbf{ON}} \\ \Huge{\textbf{MATHEMATICS}} \\[1em] Linear Algebra}
\author{\\[2em]\textit{Rao Fu \& Ying Yang}}
\date{}

\maketitle

\newpage
$ $

\newpage

\begin{minipage}[c][16cm][c]{11.5cm}
\centerline{\textit{To my parents...}}
\end{minipage}

\chapter*{Foreword}
\addcontentsline{toc}{chapter}{Foreword}

%\tableofcontents
%\listoffigures

\mainmatter

\chapter{Preliminary}
%\centerline{$e^{i \pi} + 1 = 0$}
%\[
%e^{i \pi} + 1 = 0
%\]
%\hfill {By \textit{Rao Fu}} \qquad \quad \hfill
%\\[1em]

\section{抽象代数}

\begin{quest}[{\cite{Xiong84}}]
%\label{quest:}
群的定义?
\end{quest}
满足以下条件的非空集合\ $G$ 叫做群：
\begin{enumerate}
\item
$G$ 有一个闭合的结合法，即\ $G$ 中两元\ $a,b$ 的结合\ $c$ 仍是\ $G$ 中的元；
\item
$G$ 的结合法适合结合律，即\ $G$ 中任意三元\ $a,b,c$，有\ $(ab)c=a(bc)$；
\item
$G$ 中有一个(左)单位元，对于\ $G$ 中任意元\ $a$ 有\ $ea=a$；
\item
对于$G$中任意元$a$，在$G$中有(左)逆元$a^{-1}$满足$a^{-1}a=e$；
\end{enumerate}
\begin{lem}
\label{lem:group.property.1}
任一群：
\begin{enumerate}
\item
左右逆相等(对任一元)；
\item
左右单位元相等(对任一元)；
\item
逆唯一；
\item
单位元唯一。
\end{enumerate}
\end{lem}
\begin{proof}
$ $
\begin{enumerate}
\item 即对于$a \in G$，证明若$a^{-1}a=e$，则$aa^{-1}=e$。
由于$a^{-1}aa^{-1}=ea^{-1}=a^{-1}$，因此$aa^{-1}=e$。
\item 由于$ae=aa^{-1}a=ea=a$，因此左单位元同时又是右单位元。
\item 设$b,c$都是$a$的逆元，则$ba=ca=e$，由左右逆相等，$ac=e$，则有
$b=bac=ec=c$；
\item 设$e_1,e_2$都是群的单位元，则有$e_1e_2=e_2=e_1$。
\end{enumerate}
\end{proof}
%
\begin{proof}
$ $
\begin{enumerate}
\item
设群左单位元为$e$，对元$a$有左逆元$a^{-1}$，即：
\[
\exists e, \forall a \in G: e a = a
\]
\[
\forall a \in G, \exists a^{-1}: a^{-1} a = e
\]
\[
\begin{split}
& a^{-1} a = e \\
\Rightarrow & a^{-1} a a^{-1} = e a^{-1} = a^{-1} \\
\Rightarrow & (a^{-1})^{-1} a^{-1} a a^{-1} = (a^{-1})^{-1} a^{-1} = e \\
\Rightarrow & a a^{-1} = e \\
\end{split}
\]
\item
设群左单位元为$e$，对元$a$有左逆元$a^{-1}$，即：
\[
\exists e, \forall a \in G: e a = a
\]
\[
\forall a \in G, \exists a^{-1}: a^{-1} a = e
\]
\[
\begin{split}
& a^{-1} a = e \\
\Rightarrow & a a^{-1} a = a e \\
\Rightarrow & e a = a e \\
\Rightarrow & a = a e \\
\end{split}
\]
\item
\[
\begin{split}
& b a = e;\; c a = e \\
\Rightarrow & b a = e \\
\Rightarrow & b a c = e c \\
\Rightarrow & b e = e c \\
\Rightarrow & b = c \\
\end{split}
\]
\item
\[
\exists e_1, \forall a \in G: e_1 a = a
\]
\[
\exists e_2, \forall a \in G: e_2 a = a
\]
\[
\Rightarrow e_1 e_2 = e_1 = e_2
\]
\end{enumerate}
\end{proof}

\begin{rem}
{\lemref{lem:group.property.1}}是群一个基本性质，其决定了矩阵(群)的逆唯一、左右逆相等等性质。
\end{rem}

\begin{lem}
%\label{lem:}
\[
\begin{vmatrix}
a_{11} & a_{12} & \dotsm & a_{1n} \\
a_{21} & a_{22} & \dotsm & a_{2n} \\
\dotsm & \dotsm & \dotsm & \dotsm \\
a_{n1} & a_{n2} & \dotsm & a_{nn}
\end{vmatrix}
=
\sum_{j_1 j_2 \dotsm j_n}
(-1)^{\tau(j_1 j_2 \dotsm j_n)}
\prod^n_{i=1}a_{ij_i}
\]
其中\ $\sum_{j_1 j_2 \dotsm j_n}$ 表示对所有\ $n$ 级排列求和。
\end{lem}

\begin{defn}
%\label{defn:63}
$A_{n\times n}=(\alpha_{ij})$，
如果\ $\abs{\alpha_{ii}}>\sum_{j\neq i}\abs{\alpha_{ij}},i=1,2,\dotsc,n$，
则称\ $A$ 为对角优势阵。
\end{defn}

\begin{defn}
%\label{defn:63}
$A_{n\times n}=(\alpha_{ij})$，
$A$ 的\ $t$ 阶主子阵是指位于\ $A$ 的第\ $k_1,k_2,\dotsc,k_t$ 行与第\ $k_1,k_2,\dotsc,k_t$ 列
的交叉点上元素所组成的矩阵，
记为
\[
A\begin{bmatrix}k_1,k_2,\dotsc,k_t\\k_1,k_2,\dotsc,k_t\end{bmatrix}
\]
\end{defn}

\begin{defn}
%\label{defn:63}
对角元素全为\ $0$ 的上(下)三角矩阵称为严格上(下)三角矩阵。
\end{defn}

\begin{defn}
%\label{defn:63}
位于矩阵\ $A_{n\times s}$ 的前\ $k$ 行前\ $k$ 列交叉点上的元素所成的矩阵
称为\ $A$ 的\ $k$ 阶前主子阵(顺序主子阵)，记为\ $A^{[k]}$。
\end{defn}

\begin{defn}
%\label{defn:63}
对角线元素全为\ $1$ 的上(下)三角矩阵称为单位上(下)三角矩阵。
\end{defn}

\begin{defn}
%\label{defn:63}
$A_{m\times n}=(a_{ij})$，$B_{k\times p}=(b_{ij})$，
令 $C_{m\times p}=AB$，则有
\[
c_{ij} = \sum_{k} a_{ik} b_{kj}
\]
\end{defn}

\begin{defn}
记 $E_{ij}$\ 为仅 $(i,j)$\ 元素为 $1$，其余元素均为 $0$\ 的矩阵。
\end{defn}

\begin{defn}[初等变换]
$ $

\begin{enumerate}
\item
对调矩阵任意两行：$C_{ij}$；
\item
以非零常数乘矩阵中某行：$C_i(\alpha)$；
\item
以非零常数乘矩阵中某行并加到另一行中去：$C_{ij}(k)$。
\end{enumerate}

\end{defn}

\chapter{高等代数}
\section{行列式与矩阵运算}

\begin{quest}
\label{quest:1}
分块矩阵的运算规则？
\end{quest}

\begin{quest}
\label{quest:2}
求证：
\begin{enumerate}
\item
$Ax=y$ 的充要条件为\ $y$ 是\ $A$ 的列向量的线性组合
\item
$x^TA=y^T$ 的充要条件为\ $y^T$ 是\ $A$ 的行向量的线性组合
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:3}
求证：
\begin{enumerate}
\item
$A$ 的列线性无关的充要条件为\ $Ax=0\Longrightarrow x=0$
\item
$A$ 的行线性无关的充要条件为\ $x^TA=0\Longrightarrow x=0$
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:4}
求证：$C_{n\times s}=A_{n\times k}B_{k\times s}$ 充要条件为以下之一：
\begin{enumerate}
\item
$C$ 的任意第\ $j$ 列($j=1,2,\dotsc,s$)都是\ $A$ 的列向量的线性组合，
且组合系数为\ $B$ 第\ $j$ 列的系数；
\item
$C$ 的任意第\ $i$ 行($i=1,2,\dotsc,n$)都是\ $B$ 的行向量的线性组合，
且组合系数为\ $A$ 第\ $i$ 行的系数。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:5}
设\ $A=(\alpha_{ij})$，记\ $a_j$ 是\ $A$ 的第\ $j$ 列，
$f^T_i$ 是\ $A$ 的第\ $i$ 行，
求证：
\begin{enumerate}
\item
$Ae_j=a_j$；
\item
$e^T_iA=f^T_i$；
\item
$e^T_iAe_j=\alpha_{ij}$。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:6}
求证：
\begin{enumerate}
\item
$(AB)^T=B^TA^T$；
\item
$(A_1A_2\dotsm A_{n-1}A_n)^T=A_n^TA_{n-1}^T\dotsm A_2^TA_1^T$。
\end{enumerate}
\end{quest}
%
\begin{proof}
$ $
\begin{enumerate}
\item
由矩阵乘法和转置的定义带入即可得证。
\item
由上一证明可得。
\end{enumerate}
\end{proof}

\begin{quest}
\label{quest:7}
设\ $A_i(i=1,2,\dotsc,n)$ 均为非奇异的同阶方阵，
求证：
\[
(A_1A_2\dotsm A_{n-1}A_n)^{-1}=A_n^{-1}A_{n-1}^{-1}\dotsm A_2^{-1}A_1^{-1}
\]
\end{quest}

\begin{quest}
\label{quest:8}
求证：
\[
(A^{-1})^T=(A^T)^{-1}
\]
\end{quest}

\begin{quest}
\label{quest:9}
求证：
\begin{enumerate}
\item
$\operatorname{conj}(AB)=\operatorname{conj}A \operatorname{conj}B$；
\item
$(AB)^H=B^HA^H$；
\item
$\operatorname{conj}(\alpha A)=\operatorname{conj}\alpha \operatorname{conj}A$；
\item
$(\alpha A)^H=\alpha^HA^H$；
\item
$A$ 非奇异的充要条件为\ $\bar{A}$ 非奇异或者\ $A^H$ 非奇异。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:10}
求证：
\begin{enumerate}
\item
(反)对称矩阵的和，差，数乘仍为(反)对称矩阵；
\item
$A$, $B$ 为(反)对称矩阵，则乘积\ $AB$ 为对称矩阵的充要条件为\ $AB=BA$；
\item
$k$ 正整数，当\ $A$ 为对称矩阵时，$A^k$ 仍为对称矩阵；
当\ $A$ 为反对称矩阵时，
如\ $k$ 为偶数，则\ $A^k$ 仍为对称矩阵，
如\ $k$ 为奇数，则\ $A^k$ 为反对称矩阵；
\item
对称矩阵的任一多项式仍为对称矩阵；
\item
对任意实矩阵\ $A$，$A+A^T$ 与\ $A^TA$ 为对称矩阵，$A-A^T$ 为反对称矩阵。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:11}
求证：任一实矩阵均可唯一分解成一个对称矩阵与一个反对称矩阵之和。
\end{quest}

\begin{quest}
\label{quest:12}
求证：对任何\ $x$ 均有\ $Ax=0$ 的充要条件为\ $A=0$。
\end{quest}

\begin{quest}
\label{quest:13}
求证：对任何实向量\ $x$ 均有\ $x^TBx=0$ 的充要条件为\ $B^T=-B$。
\end{quest}

\begin{quest}
\label{quest:14}
求证：
\begin{enumerate}
\item
对任何实向量\ $x$ 均有\ $x^Tx\geq 0$，且\ $x^Tx=0$ 的充要条件为\ $x=0$；
\item
对实矩阵\ $A_{n\times k}$，$A^TA=0$ 的充要条件为\ $A=0$；
\item
$A_i(i=1,2,\dotsc s)$ 为实对称矩阵，$\sum^s_{i=1}A^2_i=0$，则\ $A_i=0(i=1,2,\dotsc s)$。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:15}
求证：
\begin{enumerate}
\item
对任何复向量\ $x$ 均有\ $x^Hx\geq 0$，且\ $x^Hx=0$ 的充要条件为\ $x=0$；
\item
对复矩阵\ $A_{n\times k}$，$A^HA=0$ 的充要条件为\ $A=0$。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:16}
设\ $A$ 为实方阵，
求证：
\[
\forall x \neq 0: \frac{x^TAx}{x^Tx}=\alpha
\Longleftrightarrow
A=\alpha I+B, B^T=-B
\]
\end{quest}
\begin{proof}
考虑任一实矩阵均可唯一分解成一个对称矩阵与一个反对称矩阵之和，
并取
\[
x=e_i + e_j
\]
带入即可得证。
\end{proof}

\begin{quest}
\label{quest:17}
设\ $A$ 为实方阵，
求证：
\[
\forall x \in \mathcal{C}^n: x^HBx=0
\Longleftrightarrow
B=0
\]
\end{quest}
\begin{proof}
考虑{\questref{quest:16}}结论可知 $B$\ 必为反对称矩阵，
取
\[
x=\alpha e_i + \beta e_j, \forall \alpha, \beta \in \mathcal{C}
\]
带入则有
\[
\begin{split}
&
(\alpha e_i + \beta e_j)^H B (\alpha e_i + \beta e_j) \equiv 0 \\
\Rightarrow &
\alpha^H \beta e_i B e_j + \alpha \beta^H e_j B e_i \equiv 0 \\
\Rightarrow &
\alpha^H \beta b_{ij} + \alpha \beta^H b_{ji} \equiv 0 \\
\Rightarrow &
\alpha^H \beta b_{ij} - \alpha \beta^H b_{ij}^H \equiv 0 \\
\Rightarrow &
\alpha^H \beta b_{ij} - (\alpha^H \beta b_{ij})^H \equiv 0 \\
\Rightarrow &
\alpha^H \beta b_{ij} = (\alpha^H \beta b_{ij})^H
\end{split}
\]
即
\[
\alpha^H \beta b_{ij} \in \mathcal{R}, \forall \alpha, \beta \in \mathcal{C}
\]
则必有
\[
b_{ij} \equiv 0
\]
\end{proof}

\begin{quest}
\label{quest:18}
求证：
\begin{enumerate}
\item
$A^H=A$ 的充要条件为\ $\forall x\in\mathcal{C}^n: x^HAx\in\mathcal{R}$
\item
$A^H=A$ 的必要条件为\ $\abs{A}\in\mathcal{R}$
\end{enumerate}
\end{quest}
\begin{proof}
$ $
\begin{enumerate}
\item
\begin{itemize}
\item[$\Rightarrow$]
\[
(x^H A x)^H = x^H A^H x = x^H A x
\]
即
\[
x^H A x \in \mathcal{R}, \forall x \in \mathcal{C}^n
\]
\item[$\Leftarrow$]
\[
(x^H A x)^H = x^H A x \Rightarrow x^H (A^H - A) x = 0 \Rightarrow A = A^H
\]
\end{itemize}
\item
\[
A^H = A \Rightarrow \abs{A}^H = \abs{A} \Rightarrow \abs{A} \in \mathcal{R}
\]
\end{enumerate}
\end{proof}

\begin{quest}
\label{quest:19}
求证：
\begin{enumerate}
\item
$(A^*)^T=(A^T)^*$
\item
$(A^*)^H=(A^H)^*$
\item
$(\alpha A_{n\times n})^*=\alpha^{n-1}A^*$
\item
$A=A^T\Longrightarrow A^*={A^*}^T$，当\ $A$ 非奇异时，逆命题也成立
\item
$A\in\mathcal{R}^{n\times n},A^T=-A$，
则当\ $n$ 为偶数时\ ${A^*}^T=-A^*$，
当\ $n$ 为奇数时\ ${A^*}^T=A^*$。
\end{enumerate}
\end{quest}
\begin{proof}
符号参见{\cite{Xie99}}，
记
$S_{ij}$为$A$的余子矩阵，
$A^*=(a_{ij})$，
则有
\[
a_{ij} = (-1)^{i+j} \abs{S_{ji}}
\]
另记$S^T_{ij}$为$A^T$的余子矩阵，
$S^H_{ij}$为$A^H$的余子矩阵，则有
\[
\begin{split}
S_{ij} &= \left( S^T_{ji} \right)^T \\
S_{ij} &= \left( S^H_{ji} \right)^H
\end{split}
\]
另有
\[
A A^* = \abs{A} I
\]
带入即可得证。
\end{proof}

\begin{quest}[初等变换]
\label{quest:20}
\end{quest}
\begin{proof}
略...
\end{proof}

\begin{quest}
\label{quest:21}
$X_{p\times m}$, $Y_{m\times p}$ 为任意矩阵，求证：
\[
\begin{bmatrix}
I_m & 0   \\
X   & I_p
\end{bmatrix}
\text{和}
\begin{bmatrix}
I_m & Y   \\
0   & I_p
\end{bmatrix}
\]
可以分解成第二类初等矩阵的乘积。
\end{quest}
\begin{proof}
记 $X_{p \times m}=(\xi_{ij})$，则
\[
X = \sum^p_{i=1} \sum^m_{j=1} \xi_{ij} E_{ij}
\]
则有
\[
\begin{bmatrix}
I_m & 0   \\
X   & I_p
\end{bmatrix} =
\begin{bmatrix}
I_m & 0   \\
\sum^p_{i=1} \sum^m_{j=1} \xi_{ij} E_{ij} & I_p
\end{bmatrix} =
\prod^p_{i=1} \prod^m_{j=1}
\begin{bmatrix}
I_m & 0   \\
\xi_{ij} E_{ij} & I_p
\end{bmatrix}
\]
其中
\[
\begin{bmatrix}
I_m & 0   \\
\xi_{ij} E_{ij} & I_p
\end{bmatrix}
\]
均为初等矩阵。
\end{proof}

\begin{quest}
\label{quest:22}
$A_{n\times k}=(B_{n\times r},C)$，其中\ $C$ 的各列均是\ $B$ 的各列的线性组合，
求证：存在方阵\ $Q_{k\times k}$，为第二类初等矩阵的乘积且\ $\abs{Q}=1$，
使\ $AQ=(B,0)$。
\end{quest}
\begin{proof}
已知\ $C$ 的各列均是\ $B$ 的各列的线性组合，
则必存在 $X$，满足
\[
C = BX
\]
定义
\[
Q =
\begin{bmatrix}
I & -X \\
0 & I
\end{bmatrix}
\]
则有
\[
AQ=
\begin{bmatrix}
B & C
\end{bmatrix}
\begin{bmatrix}
I & -X \\
0 & I
\end{bmatrix}=
\begin{bmatrix}
B & 0
\end{bmatrix}
\]
另由{\questref{quest:21}}可知 $Q$\ 为第二类初等矩阵的乘积且\ $\abs{Q}=1$。
\end{proof}

\begin{quest}
\label{quest:23}
$\operatorname{rank}A_{n\times k}=r$，求证：
\begin{enumerate}
\item
有非奇异方阵\ $Q_{k\times k}$, $\abs{Q}=\pm1$，使\ $AQ=(B,0)$，
其中\ $B$ 为\ $A$ 中\ $r$ 个线性无关列组成的矩阵；
\item
有非奇异方阵\ $P_{n\times n}$, $\abs{P}=\pm1$，使\ $PA=(R;0)$，
其中\ $R$ 为\ $A$ 中\ $r$ 个线性无关行组成的矩阵；
\item
当\ $A$ 是\ $n$ 阶方阵时，存在\ $n$ 阶非奇异方阵\ $P$，
$\abs{P}=\pm1$，使\ $PAP^{-1}$ 的后\ $n-r$ 行全部为\ $0$。
\end{enumerate}
\end{quest}
\begin{proof}
略...
\end{proof}

\begin{quest}[高斯消去法]
\label{quest:24}
$x=(\xi_1;x_1)$，其中\ $\xi_1\neq0$ 为\ $n$ 元列向量\ $x$ 的第一个分量，
求证：有唯一的\ $n-1$ 元列向量\ $b$ 使
\[
\begin{bmatrix}
1 & 0 \\
b & I_{n-1}
\end{bmatrix}
x=
\begin{bmatrix}
\xi_1 \\
0
\end{bmatrix}
\]
\end{quest}
\begin{proof}
令
\[
b=- \frac{1}{\xi} x_1
\]
即可得证。
\end{proof}

\begin{quest}
\label{quest:25}
\[
G=
\begin{bmatrix}
A & B \\
C & D
\end{bmatrix}
\]
其中\ $A$ 非奇异，求证：
有矩阵\ $P$, $Q$ 均为第二类初等矩阵乘积，使
\begin{enumerate}
\item
\[
PG=
\begin{bmatrix}
A & B \\
0 & *
\end{bmatrix}
\]
\item
\[
GQ=
\begin{bmatrix}
A & 0 \\
C & *
\end{bmatrix}
\]
\item
\[
PGQ=
\begin{bmatrix}
A & 0 \\
0 & *
\end{bmatrix}
\]
\end{enumerate}
\end{quest}
\begin{proof}
$ $

\begin{enumerate}
\item
令
\[
P=
\begin{bmatrix}
I & 0 \\
-C A^{-1} & I
\end{bmatrix}
\]
则有
\[
P G=
\begin{bmatrix}
I & 0 \\
-C A^{-1} & I
\end{bmatrix}
\begin{bmatrix}
A & B \\
C & D
\end{bmatrix}
=
\begin{bmatrix}
A & B \\
0 & -C A^{-1} B + D
\end{bmatrix}
\]
\item
略...
\item
略...
\end{enumerate}
\end{proof}

\begin{quest}
\label{quest:26}
设\ $C$, $D$ 均为列线性无关矩阵，求证
\[
A=
\begin{bmatrix}
C & 0 \\
0 & D
\end{bmatrix}
\]
列线性无关。
\end{quest}
\begin{proof}
设存在 $y$，满足 $A y = 0$，把 $y$\ 按行分块：$y=(y_1;y_2)$，代入则有
\[
A y =
\begin{bmatrix}
C & 0 \\
0 & D
\end{bmatrix}
\begin{bmatrix}
y_1 \\
y_2
\end{bmatrix}
=
\begin{bmatrix}
C y_1 \\
D y_2
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0
\end{bmatrix}
\]
即 $C y_1=0$，$D y_2=0$，由已知可得 $y_1=0$, $y_2=0$，即
\[
y=0
\]
则 $A$\ 必列线性无关。
\end{proof}

\begin{quest}
\label{quest:27}
设
\[
G=
\begin{bmatrix}
A & 0 \\
0 & B
\end{bmatrix}
\]
求证：
\[
\operatorname{rank}G=
\operatorname{rank}A+
\operatorname{rank}B
\]
\end{quest}
\begin{proof}
略...
\end{proof}

\begin{quest}
\label{quest:28}
设 $A \in \mathcal{R}^{n \times n}$，且 $\operatorname{rank} A = r$，
求证：
存在 $P$，$Q$ 为初等变换的乘积，
使
\[
P A Q =
\begin{bmatrix}
I_r & 0 \\
0   & 0
\end{bmatrix}
\]
\end{quest}
\begin{proof}
$ $

\begin{enumerate}
\item
易证 $n=1$ 时显然；
\item
设 $n-1$ 时命题成立；
\item
当 $A$ 为 $n$ 阶矩阵时：若 $A$ 为零矩阵，则命题成立，否则 $A$ 必有一元非零，设 $a_{ij} \neq 0$，
则存在初等变换矩阵 $C_{1i}$ 和 $C_{1j}$ 使得
\[
C_{1i} A C_{1j} =
\begin{bmatrix}
a_{ij} & a^T \\
b      & C
\end{bmatrix}
\]
考虑到 $a_{ij} \neq 0$，则存在初等矩阵 $P_1$ 与 $Q_1$ 使得
\[
P_1
\begin{bmatrix}
a_{ij} & a^T \\
b      & C
\end{bmatrix}
Q_1 =
\begin{bmatrix}
a_{ij} & 0 \\
0      & D
\end{bmatrix}
\]
其中 $D$ 为 $n-1$ 阶矩阵，且 $\operatorname{rank} D = r - 1$。
根据归纳法假设，必存在初等矩阵乘积 $S$ 与 $R$ 使得
\[
S D R =
\begin{bmatrix}
I_{r-1} & 0 \\
0       & 0
\end{bmatrix}
\]
去
\[
\begin{split}
P &=
\begin{bmatrix}
a_{ij}^{-1} & 0 \\
0           & I_{n-1}
\end{bmatrix}
\begin{bmatrix}
1 & 0 \\
0 & S
\end{bmatrix}
P_1 C_{1i} \\
Q &=
C_{1j} Q_1
\begin{bmatrix}
1 & 0 \\
0 & R
\end{bmatrix}
\end{split}
\]
显然 $P$，$Q$ 为初等矩阵乘积，且有
\[
P A Q =
\begin{bmatrix}
I_r & 0 \\
0   & 0
\end{bmatrix}
\]
\end{enumerate}
\end{proof}

\begin{quest}
\label{quest:29}
\end{quest}

\begin{quest}
\label{quest:30}
设\ $\operatorname{rank}A_{n\times k}=r$，求证：
\begin{enumerate}
\item
存在\ $M_{n\times r}$,
$N_{r\times k}$ 满足\ $\operatorname{rank}M=\operatorname{rank}N=r$，
且\ $A=MN$
\item
存在\ $R_{n\times k}$,
$S_{k\times k}$ 满足\ $\operatorname{rank}R=\operatorname{rank}S=r$，
且\ $A=RS$
\item
存在\ $R_{n\times n}$,
$S_{n\times k}$ 满足\ $\operatorname{rank}R=\operatorname{rank}S=r$，
且\ $A=RS$
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:31}
求证：$\abs{A_{n\times n}}=1$ 充要条件为\ $A$ 可表示成第二类初等矩阵的乘积。
\end{quest}

\begin{quest}
\label{quest:32}
$A$ 与对角元互异的对角阵\ $G$ 乘法可换，求证：$A$ 必为对角阵。
\end{quest}

\begin{quest}
\label{quest:33}
求证：$A$ 为纯量矩阵(即\ $A=\alpha I_n$)的充要条件为\ $A$ 与任何非奇异矩阵乘法可换。
\end{quest}

\begin{quest}
\label{quest:34}
求证：$A$ 为纯量矩阵的充要条件为\ $A$ 与所有形如\ $E_{ij}=e_ie_j^T,i,j=1,2,\dotsc,n$ 的矩阵乘法可换。
\end{quest}

\begin{quest}
\label{quest:35}
求证：$A$ 为纯量矩阵的充要条件为
对一切非零复向量\ $x$ 均有
\[
\frac{x^HAx}{x^Hx}\equiv\alpha
\]
\end{quest}

\begin{quest}
\label{quest:36}
设\ $A=PCP^{-1},B=PDP^{-1}$，求证\ $A,B$ 可换的充要条件为\ $C,D$ 可换。
\end{quest}

\begin{quest}
\label{quest:37}
设\ $X_i,i=1,2,\dotsc,k$ 为\ $n_i$ 阶方阵。
求证：
$X=\operatorname{diag}_iX_i$ 的充要条件为\ $X$ 与所有形如\ $A=\operatorname{diag}_i\alpha_iI_{n_i},\alpha_i\in\mathcal{R}$ 的
矩阵乘法可换。
\end{quest}

\begin{quest}
\label{quest:38}
%设
%\[
%f(\lambda)=\alpha_k\lambda^k+\alpha_{k-1}\lambda^{k-1}+\dotsb+\alpha_1\lambda+\alpha_0
%\]
关于矩阵\ $A$ 的任意两个矩阵多项式乘积可换。
\end{quest}

\begin{quest}
\label{quest:39}
求证：
\begin{enumerate}
\item
上(下)三角矩阵的积、和、差、数乘仍为上(下)三角矩阵；
\item
上(下)三角矩阵的矩阵多项式仍为上(下)三角矩阵；
\item
$A$ 既为上三角矩阵，又是下三角矩阵，则\ $A$ 为对角阵。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:40}
求证：上(下)三角矩阵非奇异的充要条件是它的的对角元全部非零。
\end{quest}

\begin{quest}
\label{quest:41}
设\ $A=(\alpha_{ij})$ 为上(下)三角矩阵，求证：$A^*$ 也为上(下)三角矩阵。
\end{quest}

\begin{quest}
\label{quest:42}
求证：
\begin{enumerate}
\item
非奇异矩阵\ $A$ 为上(下)三角矩阵的充要条件为\ $A^{-1}$ 也是上(下)三角矩阵，
且\ $A$ 与\ $A^{-1}$ 对应的对角元互为倒数；
\item
$A$ 非奇异时，{\questref{quest:41}} 的逆命题也成立；
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:43}
$AB=C$，其中\ $C$ 为上(下)三角矩阵，求证：
当\ $A$, $B$ 之一为非奇异上(下)三角矩阵时，另一个必为上(下)三角矩阵。
\end{quest}

\begin{quest}
\label{quest:44}
设有分块上三角矩阵
\[
A=
\begin{bmatrix}
A_1             &                 &                 & *   \\
                & A_2             &                 &     \\
                &                 & \ddots          &     \\
                &                 &                 & A_s
\end{bmatrix}
\]
其中\ $A_i,i=1,2,\dotsc,s$ 为\ $n_i$ 阶方阵，求证：
\begin{enumerate}
\item
分块上(下)三角矩阵的任何\ $k$ 次方仍为分块上(下)三角矩阵，且
\[
A^k=
\begin{bmatrix}
A_1^k           &                 &                 & *   \\
                & A_2^k           &                 &     \\
                &                 & \ddots          &     \\
                &                 &                 & A_s^k
\end{bmatrix}
\]
\item
设
\[
B=
\begin{bmatrix}
B_1             &                 &                 & *   \\
                & B_2             &                 &     \\
                &                 & \ddots          &     \\
                &                 &                 & B_s
\end{bmatrix}
\]
则
\[
\begin{split}
A+B&=
\begin{bmatrix}
A_1+B_1         &                 &                 & *   \\
                & A_2+B_2         &                 &     \\
                &                 & \ddots          &     \\
                &                 &                 & A_s+B_s
\end{bmatrix}\\
AB&=
\begin{bmatrix}
A_1B_1          &                 &                 & *   \\
                & A_2B_2          &                 &     \\
                &                 & \ddots          &     \\
                &                 &                 & A_sB_s
\end{bmatrix}
\end{split}
\]
\item
分块上(下)三角矩阵的任一多项式仍为分块上(下)三角矩阵，即
\[
f(A)=
\begin{bmatrix}
f(A_1)          &                 &                 & *   \\
                & f(A_2)          &                 &     \\
                &                 & \ddots          &     \\
                &                 &                 & f(A_s)
\end{bmatrix}
\]
\item
分块对角矩阵的任一多项式仍为分块对角矩阵。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:45}
当\ $A$ 为严格上(下)三角矩阵时，求证：
\begin{enumerate}
\item
$A$ 与上(下)三角矩阵的乘积仍为严格上(下)三角矩阵；
\item
设\ $k$ 为正整数，记\ $A^k=(\alpha^{(k)}_{ij})$，则对\ $j<i+k$ 有\ $\alpha^{(k)}_{ij}=0$。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:46}
$A=(\alpha_{ij})$ 为严格上(下)三角矩阵，求证：
\begin{enumerate}
\item
$A^{n-1}$ 只有右(左)上角一个元素可能非\ $0$，
它等于\ $A$ 的上(下)对角线元素乘积，即
\[
\alpha_{12}\alpha_{23}\dotsm\alpha_{n-1,n}
\]
或
\[
\alpha_{21}\alpha_{32}\dotsm\alpha_{n,n-1}
\]
其余元素全部为\ $0$；
\item
$A^n=0$。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:47}
$A$ 的定义同{\questref{quest:44}}，求证：
\begin{enumerate}
\item
$A$ 非奇异的充要条件为\ $A_i,i=1,2,\dotsc,s$ 均非奇异；
\item
$A$ 非奇异时，$A^{-1}$ 仍为分块上三角矩阵，且具有形式：
\[
A^{-1}=
\begin{bmatrix}
A_1^{-1}        &                 &                 & *   \\
                & A_2^{-1}        &                 &     \\
                &                 & \ddots          &     \\
                &                 &                 & A_s^{-1}
\end{bmatrix}
\]
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:48}
设\ $B$ 为上三角矩阵，$C$ 为下三角矩阵，求证：
\begin{enumerate}
\item
$(AB)^{[k]}=A^{[k]}B^{[k]}$；
\item
$(CA)^{[k]}=C^{[k]}A^{[k]}$。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:49}
设\ $A_{n\times n}$ 为非奇异上(下)三角矩阵，求证：
\[
\left( A^{[k]} \right)^{-1}=\left( A^{-1} \right)^{[k]}
\]
\end{quest}

\begin{quest}
\label{quest:50}
$A=D-U$，其中\ $D$ 为\ $n$ 阶非奇异对角阵，$U$ 为\ $n$ 阶严格上三角矩阵，求证：
\[
A^{-1}=
D^{-1}
\left[
I+UD^{-1}+\left(UD^{-1}\right)^2+\dotsb+\left(UD^{-1}\right)^{n-1}
\right]
\]
\end{quest}

\begin{quest}
\label{quest:51}
求证：
\begin{enumerate}
\item
单位上(下)三角矩阵的乘积仍为单位上(下)三角矩阵；
\item
单位上(下)三角矩阵一定非奇异，且逆阵也是单位上(下)三角矩阵；
\item
对任何整数\ $k$，单位上(下)三角矩阵的\ $k$ 次方也是单位上(下)三角矩阵；
\item
$A$ 既为单位上三角矩阵，又为单位下三角矩阵，则\ $A=I$。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:52}
如果\ $A$ 非奇异，且可分解为
\[
A=LDU
\]
其中\ $L$ 为单位下三角矩阵，
$D$ 为对角阵，$U$ 为单位上三角矩阵。求证：该分解形式唯一。
\end{quest}

\begin{quest}
\label{quest:53}
条件同{\questref{quest:52}}，求证：$A$ 的所有\ $k$ 阶顺序主子阵均非奇异。
\end{quest}

\begin{quest}
\label{quest:54}
$A$ 为非奇异的对称矩阵，且有{\questref{quest:52}} 中分解式，求证：
\[
L=U^T
\]
\end{quest}

\begin{quest}
\label{quest:55}
设\ $A^k=0,k\in\mathcal{N}$，求证：$I-A$ 非奇异。
\end{quest}

\begin{quest}
\label{quest:56}
$u,v\in\mathcal{R}^n,\gamma\neq0,\beta\neq0,v^Tu=\gamma^{-1}+\beta^{-1}$，
求证：$I-\beta uv^T$ 非奇异，且
\[
\left(I-\beta uv^T\right)^{-1}=I-\gamma uv^T
\]
\end{quest}

\begin{quest}
\label{quest:57}
矩阵\ $B_{n\times n},S_{k\times k},M_{k\times k}$ 均非奇异，
$V^T_{k\times n}B^{-1}U_{n\times k}=S^{-1}+M^{-1}$，求证：
\[
\left(
B-USV^T
\right)^{-1}=B^{-1}-B^{-1}UMV^TB^{-1}
\]
\end{quest}

\begin{quest}
\label{quest:58}
$A_{n \times n}$ 非奇异，$A$ 的每行元素之和为常数\ $\alpha$, 求证：
\begin{enumerate}
\item
$\alpha \neq 0$
\item
$A^{-1}$ 的每行元素之和为常数\ $\alpha^{-1}$
\end{enumerate}
\end{quest}
\begin{proof}
$ $

\begin{enumerate}
\item
将\ $A$ 的各列加到第一列上，其行列式按第一列展开，则有
\[
\det A=a(A_{11}+A_{21}+\dotsb+A_{n1})
\]
其中\ $A_{i1},i=1,2,\dotsc,n$ 为初等变换后矩阵第一列各元素的代数余子式。
由于\ $\det A \neq 0$，因此\ $a \neq 0$。
\item
由于
\[
A^{-1}=
\dfrac{1}{\det A}
\begin{bmatrix}
A_{11} & A_{21} & \cdots & A_{n1} \\
A_{12} & A_{22} & \cdots & A_{n2} \\
\hdotsfor{4}                      \\
A_{1n} & A_{2n} & \cdots & A_{nn}
\end{bmatrix}
\]
则其第一行元素之和为
\[
\dfrac{1}{\det A}(A_{11}+A_{21}+\dotsb+A_{n1})=a^{-1}
\]
在\ 1 中，若将\ $A$ 的各列加到第二列上并将其行列式按第二列展开，则有
\[
\det A=a(A_{12}+A_{22}+\dotsb+A_{n2})
\]
可证\ $A^{-1}$ 的第二行元素之和也为\ $a^{-1}$。
类似地可证\ $A^{-1}$ 的其它各行元素之和均为\ $a^{-1}$。
\end{enumerate}
\end{proof}

\begin{quest}
\label{quest:59}
已知\ $n$ 个\ $n$ 阶方阵\ $E_i=\beta_ie_ie_i^T,i=1,2,\dotsc,n$，求证：$k\geq2$ 时
\[
\sum_{(i_1i_2\dotsm i_k)}E_{i_1}E_{i_2}\dotsm E_{i_k}=0
\]
其中\ $(i_1i_2\dotsm i_k)$ 是\ $1,2,\dotsc,n$ 中取\ $k$ 个元素的一个组合。
\end{quest}

\begin{quest}
\label{quest:60}
求证：任何一个\ $n$ 阶方阵均可表为形如\ $I+\alpha_{ij}e_ie_j^T$ 的矩阵的乘积。
\end{quest}

\begin{quest}
\label{quest:61}
设
\[
A=
\begin{bmatrix}
P & Q \\
0 & I
\end{bmatrix}
\]
其中\ $P$ 为方阵，求证：
\begin{enumerate}
\item
若\ $P-I$ 非奇异，则对任何正整数\ $k$，均有
\[
A^k=
\begin{bmatrix}
P^k & Q_k \\
0 & I
\end{bmatrix}
\]
其中
\[
Q_k=(P^k-I)(P-I)^{-1}Q
\]
\item
若\ $P$ 也非奇异，则上式对于一切负整数也成立，即
\[
A^{-k}=
\begin{bmatrix}
P^{-k} & Q_{-k} \\
0      & I
\end{bmatrix}
\]
其中
\[
Q_{-k}=(P^{-k}-I)(P-I)^{-1}Q
\]
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:62}
设
\[
A=
\begin{bmatrix}
-\alpha_1 & -\alpha_2 & \dotsm & -\alpha_{n-1} & -\alpha_n \\
1         & 0         & \dotsm & 0             & 0         \\
0         & 1         & \dotsm & 0             & 0         \\
\dotsm    & \dotsm    & \dotsm & \dotsm        & \dotsm    \\
0         & 0         & \dotsm & 1             & 0
\end{bmatrix}
\]
求证：当\ $\alpha_n\neq0$ 时，$A$ 非奇异并求\ $A^{-1}$。
\end{quest}

\begin{quest}
\label{quest:63}
$A_{n\times n}=(\alpha_{ij})$，求证：
\begin{enumerate}
\item
$A$ 为对角优势阵时，则\ $A$ 的任一\ $t$ 阶主子阵仍为对角优势阵；
\item
$A$ 经一步高斯消去法以后变为
\[
A'=\begin{bmatrix}\alpha_{11}&a^T\\0&A_{22}\end{bmatrix}
\]
则\ $A_{22}$ 仍为对角优势阵；
\item
若\ $A$ 还具有正对角元，则\ $A_{22}$ 也具有正对角元。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:64}
$A_{n \times n}$ 的元素均为整数, 求证：$A^{-1}$ 的元素均为整数当且仅当
\[
\det{A}=\pm1
\]
\end{quest}
\begin{proof}
$ $
\begin{description}
\item[$\Longleftarrow$]

由于\ $A$ 的元素均为整数，因此其伴随矩阵\ $A^*$ 的元素也均为整数。
而\ $A^{-1}=\dfrac{1}{\det{A}}A^*=\pm A^*$，因此\ $A^{-1}$ 的元素均为整数。
\item[$\Longrightarrow$]

由于\ $A$ 与\ $A^{-1}$ 的元素均为整数，则\ $\det{A}$ 与\ $\det{A^{-1}}$ 均为整数，
而\ $\det{A}\det{A^{-1}}=\det{A}\dfrac{1}{\det A}=1$，因此\ $\det{A}=\pm 1$。
\end{description}
\end{proof}

\begin{quest}
\label{quest:65}
排列\ $\alpha_1 \alpha_2 \dotsm \alpha_n$ 的逆序数为\ $s$，
求：排列\ $\alpha_n \alpha_{n-1} \dotsm \alpha_1$ 的逆序数。
\end{quest}
\begin{proof}
一个\ $n$ 级排列的最大逆序数为\ $n-1+n-2+\dotsb+1=n(n-1)/2$，
它等于\ $\alpha_1 \alpha_2 \dotsm \alpha_n$ 的逆序数
与\ $\alpha_n \alpha_{n-1} \dotsm \alpha_1$ 的逆序数之和，
所以\ $\alpha_n \alpha_{n-1} \dotsm \alpha_1$ 的逆序数为\ $n(n-1)/2-s$。
\end{proof}

\begin{quest}
\label{quest:66}
证明：奇偶排列各占一半。
\end{quest}
\begin{proof}
由定义可知，$n$ 级行列式等于所有取自不同行不同列的\ $n$ 个元素的乘积\ $a_{1j_1}a_{1j_2}\dotsm a_{1j_n}$ 的代数和，
其中\ $j_1j_2\dotsm j_n$ 是\ $1,2,\dotsm,n$ 的一个排列，
当其为偶排列时，该乘积带正号，奇排列时带符号。由于
\[
\begin{bmatrix}
1      & 1      & \dotsm & 1      \\
1      & 1      & \dotsm & 1      \\
\dotsm & \dotsm & \dotsm & \dotsm \\
1      & 1      & \dotsm & 1
\end{bmatrix}
=
\sum_{j_1 j_2 \dotsm j_n}(-1)^{\tau(j_1 j_2 \dotsm j_n)} = 0
\]
其中\ $\sum_{j_1 j_2 \dotsm j_n}$ 表示对所有\ $n$ 级排列求和。因此奇偶排列各占一半。
\end{proof}

\begin{quest}
\label{quest:67}
求：
\[
\sum_{j_1 j_2 \dotsm j_n}
\begin{vmatrix}
a_{1j_1} & a_{1j_2} & \dotsm & a_{1j_n} \\
a_{2j_1} & a_{2j_2} & \dotsm & a_{2j_n} \\
\dotsm   & \dotsm   & \dotsm & \dotsm   \\
a_{nj_1} & a_{nj_2} & \dotsm & a_{nj_n}
\end{vmatrix}
\]
其中\ $\sum_{j_1 j_2 \dotsm j_n}$ 表示对所有\ $n$ 级排列求和。
\end{quest}
\begin{proof}
\[
\begin{split}
&
\sum_{j_1 j_2 \dotsm j_n}
\begin{vmatrix}
a_{1j_1} & a_{1j_2} & \dotsm & a_{1j_n} \\
a_{2j_1} & a_{2j_2} & \dotsm & a_{2j_n} \\
\dotsm   & \dotsm   & \dotsm & \dotsm   \\
a_{nj_1} & a_{nj_2} & \dotsm & a_{nj_n}
\end{vmatrix}\\
=&
\sum_{j_1 j_2 \dotsm j_n}
(-1)^{\tau(j_1 j_2 \dotsm j_n)}
\begin{vmatrix}
a_{11} & a_{12} & \dotsm & a_{1n} \\
a_{21} & a_{22} & \dotsm & a_{2n} \\
\dotsm & \dotsm & \dotsm & \dotsm \\
a_{n1} & a_{n2} & \dotsm & a_{nn}
\end{vmatrix}\\
=&
\sum_{j_1 j_2 \dotsm j_n}
(-1)^{\tau(j_1 j_2 \dotsm j_n)}
\sum_{k_1 k_2 \dotsm k_n}
(-1)^{\tau(k_1 k_2 \dotsm k_n)}
\prod^n_{i=1}a_{ik_i}\\
=&
\sum_{k_1 k_2 \dotsm k_n}
(-1)^{\tau(k_1 k_2 \dotsm k_n)}
\prod^n_{i=1}a_{ik_i}
\left(
\sum_{j_1 j_2 \dotsm j_n}
(-1)^{\tau(j_1 j_2 \dotsm j_n)}
\right)\\
=&
\sum_{k_1 k_2 \dotsm k_n}
(-1)^{\tau(k_1 k_2 \dotsm k_n)}
\prod^n_{i=1}a_{ik_i}
0\\
=&0
\end{split}
\]
\end{proof}

\begin{quest}
\label{quest:68}
将\ $n$ 位的\ $t$ 进制数\ $a = a_{n-1} t^{n-1} + a_{n-2} t^{n-2} + \dotsb + a_{1} t + a_{0}$ 记为
\[
a = \overline{a_{n-1} a_{n-2} \dotsm a_{0}}
\]
求证：当
\[
a_i = \overline{a_{n-1}^{(i)} a_{n-2}^{(i)} \dotsm a_{0}^{(i)}},\,i=1,2,\dotsc,n
\]
均被整数\ $m$ 整除，则行列式
\[
d =
\begin{vmatrix}
a_{n-1}^{(1)} & a_{n-2}^{(1)} & \dotsm & a_{0}^{(1)} \\
a_{n-1}^{(2)} & a_{n-2}^{(2)} & \dotsm & a_{0}^{(2)} \\
\dotsm        & \dotsm        & \dotsm & \dotsm      \\
a_{n-1}^{(n)} & a_{n-2}^{(n)} & \dotsm & a_{0}^{(n)}
\end{vmatrix}
\]
能被\ $m$ 整除。
\end{quest}
\begin{proof}
定义
\[
D \triangleq
\begin{bmatrix}
a_{n-1}^{(1)} & a_{n-2}^{(1)} & \dotsm & a_{0}^{(1)} \\
a_{n-1}^{(2)} & a_{n-2}^{(2)} & \dotsm & a_{0}^{(2)} \\
\dotsm        & \dotsm        & \dotsm & \dotsm      \\
a_{n-1}^{(n)} & a_{n-2}^{(n)} & \dotsm & a_{0}^{(n)}
\end{bmatrix},\quad
E \triangleq
\begin{bmatrix}
1 & 0 & \dotsm & t^{n-1} \\
0 & 1 & \dotsm & t^{n-2} \\
\dotsm & \dotsm & \dotsm & \dotsm \\
0 & 0 & \dotsm & 1
\end{bmatrix}
\]
由于
\[
\begin{aligned}
d &= \det D = \det D \det E = \det DE \\
  &= \begin{vmatrix}
  a_{n-1}^{(1)} &  a_{n-2}^{(1)} & \cdots  & a_1 \\
  a_{n-1}^{(2)} &  a_{n-2}^{(2)} & \cdots & a_2 \\
  \hdotsfor{4} \\
  a_{n-1}^{(n)} &  a_{n-2}^{(n)} & \cdots & a_n
  \end{vmatrix} \\
   &=\sum_{k_1k_2 \dotsm k_{n-1}}(-1)^{\tau(k_1k_2 \dotsm k_{n-1})} \prod_j a_j \prod_{i \neq j}a_{n-k_i}^{(i)}\quad{\color{red}\text{似乎不对？}} \\
   &=\sum_{k_1k_2 \dotsm k_n} \left( (-1)^{\tau(k_1k_2 \dotsm k_n)} a_{k_n} \prod_{i=1}^{n-1} a_{n-i}^{(k_i)} \right)
\end{aligned}
\]
由于\ $a_j,j=1,2,\dotsc,n$ 能被\ $m$ 整除，因此行列式能被\ $m$ 整除。
\end{proof}

\begin{quest}
\label{quest:69}
奇数阶反对称矩阵必奇异。
\end{quest}
\begin{proof}
由矩阵反对称可知其元素满足$a_{ij}=-a_{ji}, a_{ii}=0, i,j=1,2,\dotsc,n$。其行列式
\[
\begin{aligned}
d &=\begin{vmatrix}
0       & a_{12} & a_{13} & \dotsm & a_{1n} \\
-a_{12} & 0      & a_{23} & \dotsm & a_{2n} \\
\hdotsfor{5} \\
-a_{1n} & -a_{2n} & -a_{3n} & \dotsm & 0
\end{vmatrix} \\
& =\begin{vmatrix}
0       & -a_{12} & -a_{13} & \dotsm & -a_{1n} \\
a_{12}  & 0       & -a_{23} & \dotsm & -a_{2n} \\
\hdotsfor{5} \\
a_{1n} & a_{2n} & a_{3n} & \dotsm & 0
\end{vmatrix} \\
& =(-1)^n \begin{vmatrix}
0       & a_{12} & a_{13} & \dotsm & a_{1n} \\
-a_{12} & 0      & a_{23} & \dotsm & a_{2n} \\
\hdotsfor{5} \\
-a_{1n} & -a_{2n} & -a_{3n} & \dotsm & 0
\end{vmatrix}\\
& =(-1)^nd
\end{aligned}
\]
当\ $n$ 为奇数时，$d=-d$，因而\ $d=0$。
\end{proof}

\begin{quest}
\label{quest:70}
设
\[
F(t) =
\begin{vmatrix}
f_{11}(t) & f_{12}(t) & \dotsm & f_{1n}(t) \\
f_{21}(t) & f_{22}(t) & \dotsm & f_{2n}(t) \\
\dotsm    & \dotsm    & \dotsm & \dotsm    \\
f_{n1}(t) & f_{n2}(t) & \dotsm & f_{nn}(t)
\end{vmatrix}
\]
求证：
\[
\frac{d}{dt} F(t) = \sum_{j=1}^n D_j (t)
\]
其中
\[
D_j (t) =
\begin{vmatrix}
f_{11}(t) & f_{12}(t) & \dotsm & \displaystyle{\frac{d}{dt} f_{1j}(t)} & \dotsm & f_{1n}(t) \\
f_{21}(t) & f_{22}(t) & \dotsm & \displaystyle{\frac{d}{dt} f_{2j}(t)} & \dotsm & f_{2n}(t) \\
\dotsm    & \dotsm    & \dotsm & \dotsm                                & \dotsm & \dotsm    \\
f_{n1}(t) & f_{n2}(t) & \dotsm & \displaystyle{\frac{d}{dt} f_{nj}(t)} & \dotsm & f_{nn}(t)
\end{vmatrix}
\]
\end{quest}
\begin{proof}
{\color{red}提示: 拉普拉斯定理。$n$ 级行列式等于所有取自不同行不同列的几个元素的乘积的代数和。}

根据行列式定义有：
\[
\begin{split}
\frac{d}{dt} F(t) &=
\frac{d}{dt}
\begin{vmatrix}
f_{11}(t) & f_{12}(t) & \dotsm & f_{1n}(t) \\
f_{21}(t) & f_{22}(t) & \dotsm & f_{2n}(t) \\
\dotsm    & \dotsm    & \dotsm & \dotsm    \\
f_{n1}(t) & f_{n2}(t) & \dotsm & f_{nn}(t)
\end{vmatrix} \\
&=
\frac{d}{dt} \sum_{k_1k_2\dotsm k_n} \left( (-1)^{\tau(k_1 k_2 \dotsm k_n)} \prod_{i} f_{k_ii}(t) \right) \\
&=
\sum_{k_1k_2\dotsm k_n} \left( (-1)^{\tau(k_1 k_2 \dotsm k_n)} \frac{d}{dt} \prod_{i} f_{k_ii}(t) \right) \\
&=
\sum_{k_1k_2\dotsm k_n} \left( (-1)^{\tau(k_1 k_2 \dotsm k_n)} \sum_{j} \left( \frac{d}{dt} f_{k_jj}(t) \prod_{i\neq j} f_{k_ii}(t) \right) \right) \\
&=
\sum_{j} \left( \sum_{k_1k_2\dotsm k_n} (-1)^{\tau(k_1 k_2 \dotsm k_n)} \frac{d}{dt} f_{k_jj}(t) \prod_{i\neq j} f_{k_ii}(t) \right) {\quad\color{red}\text{Fixed.}} \\
&=
\sum_{j} D_j(t)
\end{split}
\]
\end{proof}

\begin{quest}
\label{quest:71}
设
\[
P(\lambda) =
\begin{vmatrix}
1      & \lambda & \lambda^2 & \dotsm & \lambda^{n-1} \\
1      & a_1     & a_1^2     & \dotsm & a_1^{n-1}     \\
\dotsm & \dotsm  & \dotsm    & \dotsm & \dotsm        \\
1      & a_{n-1} & a_{n-1}^2 & \dotsm & a_{n-1}^{n-1}
\end{vmatrix}
\]
其中\ $a_i,\,i=1,2,\dotsc,n-1$ 互不相等，
求证：$P(\lambda)$ 是\ $\lambda$ 的\ $n-1$ 次多项式，并求根。
\end{quest}
\begin{proof}
对\ $P(\lambda)$ 做初等变换，则
\[
P(\lambda) =
\begin{vmatrix}
1            & 1       & \dotsm    & 1  \\
\lambda      & a_1     &    \dotsm & a_{n-1}     \\
\lambda^2    & a_1^2   & \dotsm    & a_{n-1}^2 \\
\hdotsfor{4} \\
\lambda^{n-1}& a_1^{n-1} & \dotsm & a_{n-1}^{n-1} \\
\end{vmatrix}
\]
是一个\ $n$ 级的范德蒙行列式，则有
\[
P(\lambda)=\prod_{1 \le i \le n-1}(a_i-\lambda)\prod_{1 \le j < i \le n-1}(a_i-a_j)
\]
因此\ $P(\lambda)$ 是\ $\lambda$ 的\ $n-1$ 次多项式，
其根为\ $a_i,i=1,2,\dotsc,n-1$。
\end{proof}

\begin{quest}
\label{quest:72}
求证：
\[
\begin{vmatrix}
1        & 0        & \dotsm & 0        & \beta_1 \\
0        & 1        & \dotsm & 0        & \beta_2 \\
\dotsm   & \dotsm   & \dotsm & \dotsm   & \dotsm  \\
0        & 0        & \dotsm & 1        & \beta_n \\
\alpha_1 & \alpha_2 & \dotsm & \alpha_n & 0
\end{vmatrix}
=
- \left( \alpha_1 \beta_1 + \alpha_2 \beta_2 + \dotsm + \alpha_n \beta_n \right)
\]
\end{quest}
\begin{proof}
将行列式按最后一列展开，有
\[
\begin{vmatrix}
1        & 0        & \dotsm & 0        & \beta_1 \\
0        & 1        & \dotsm & 0        & \beta_2 \\
\hdotsfor{5} \\
0        & 0        & \dotsm & 1        & \beta_n \\
\alpha_1 & \alpha_2 & \dotsm & \alpha_n & 0
\end{vmatrix}
=\beta_1A_{1n}+\beta_2A_{2n}+\dotsb+\beta_nA_{nn}
\]
其中\ $A_{in},i=1,2,\dotsc,n$ 为\ $\beta_i$ 的代数余子式。又
\[
A_{1n}=(-1)^{2+n}\begin{vmatrix}
0        & 1        & 0      & \dotsm & 0   \\
0        & 0        & 1      & \dotsm & 0   \\
\hdotsfor{5} \\
0        & 0        & 0      & \dotsm & 1    \\
\alpha_1 & \alpha_2 & \dotsm & \dotsm & \alpha_n
\end{vmatrix}
\]
将上式中的行列式按第一列展开，则有
\[
A_{1n}=(-1)^{2+n}(-1)^{n+1}\alpha_1=-\alpha_1
\]
依此类推，
将\ $A_{in}$ 中的行列式按第\ $i$ 列展开，
可得
\[
A_{in}=-\alpha_i
\]
由此可证原行列式等于\ $- \left( \alpha_1 \beta_1 + \alpha_2 \beta_2 + \dotsm + \alpha_n \beta_n \right)$。
\end{proof}

\begin{quest}
\label{quest:73}
求证：
\begin{enumerate}
\item
\[
\begin{vmatrix} A & y \\ x^T & 0 \end{vmatrix} = - x^T A^* y
\]
其中\ $x = (x_1, x_2, \dotsm, x_n)^T$，
$y = (y_1, y_2, \dotsm, y_n)^T$
\item
\[
\begin{vmatrix} A & y \\ x^T & \alpha \end{vmatrix} = \alpha \det{A} - x^T A^* y
\]
当\ $A$ 非奇异时
\item
\[
\begin{vmatrix} A & y \\ x^T & \alpha \end{vmatrix} = \left( \alpha - x^T A^{-1} y \right) \det{A}
\]
\end{enumerate}
\end{quest}
\begin{proof}
$ $

\begin{enumerate}
\item
取行列式的前\ $n$ 行，
由这\ $n$ 行元素组成的\ $n+1$ 个\ $n$ 级子式记为\ $M_1,\dotsc,M_{n+1}$，
它们的代数余子式分别为
\[
\begin{aligned}
A_1&=(-1)^{(1+\dotsb+n)+(2+\dotsb+n+1)}x_1   \\
A_2&=(-1)^{(1+\dotsb+n)+(1+3+\dotsb+n+1)}x_2 \\
   & \mspace{100mu} \vdots                   \\
A_n&=(-1)^{n-1}x_n                           \\
A_{n+1}&=0
\end{aligned}
\]
由拉普拉斯定理可得
\[
\begin{vmatrix}
A & y \\
x^T & 0
\end{vmatrix}
=
\sum_{j=1}^n A_jM_j
\]
又
\[
M_j
=
\begin{vmatrix}
a_{11} & \dotsm & a_{1(j-1)} & a_{1(j+1)}& \dotsm & a_{1n} & y_1\\
a_{21} & \dotsm & a_{2(j-1)} & a_{2(j+1)}& \dotsm & a_{2n} & y_2\\
\hdotsfor{7} \\
a_{n1} & \dotsm & a_{n(j-1)} & a_{n(j+1)}& \dotsm & a_{nn} & y_n\\
\end{vmatrix}
\]
将\ $M_j$ 按最后一列展开，则
\[
M_j=\sum_{i=1}^n (-1)^{n-j}y_j M_{ij}',j=1,2,\dotsc,n
\]
其中\ $M_{ij}'$ 是\ $A$ 的元素\ $a_{ij}$ 的代数余子式，因此
\[
\begin{vmatrix} A & y \\ x^T & 0 \end{vmatrix} = \sum_{j=1}^n \sum_{i=1}^n(-1)^{n-1} x_jM_{ij}'y_j={\color{red}(-1)^{n-1}x^TA^*y}
\]
\item
和\ 1 证法类似，此时\ $A_{n+1}=\alpha \det A$
\[
\begin{vmatrix}
A & y \\
x^T & \alpha
\end{vmatrix}
=
\begin{vmatrix}
A & y \\
x^T & 0
\end{vmatrix}+
\alpha \det A=\alpha \det A-x^TA^*y
\]
\item
由于\ $A^*= A^{-1}\det A$，代入\ 2 可得\ 3。
\end{enumerate}
\end{proof}

\begin{quest}
\label{quest:74}
$A$ 为方阵，若
\[
\begin{vmatrix}
A & a \\
b^T & \beta
\end{vmatrix}
=0
\]
求证：
\[
\begin{vmatrix}
A & a \\
b^T & \gamma
\end{vmatrix}
=(\gamma-\beta)\abs{A}
\]
\end{quest}

\begin{quest}
\label{quest:75}
$A$ 奇异，令
\[
A=
\begin{bmatrix}
A^{[n-1]} & a \\
b^T       & \alpha_{nn}
\end{bmatrix}
\]
其中\ $A^{[n-1]}$ 非奇异，记
\[
A(\varepsilon)=
\begin{bmatrix}
A^{[n-1]} & a \\
b^T       & \alpha_{nn}+\varepsilon
\end{bmatrix}
\]
求证：对任何\ $\varepsilon\neq0$ 均有\ $A(\varepsilon)$ 非奇异；
且当\ $\abs{A^{[n-1]}}>0,\varepsilon>0$ 时，$\abs{A(\varepsilon)}>0$。
\end{quest}

\begin{quest}
\label{quest:76}
$A=(B,C)$，$C^TB=0$，求证：
\[
\abs{A^TA}=\abs{B^TB}\abs{C^TC}
\]
\end{quest}

\begin{quest}
\label{quest:77}
求证：
\[
\det{AB} = \det{A} \det{B}
\]
\end{quest}
\begin{proof}
设
\begin{gather*}
A=\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\
                a_{21} & a_{22} & \cdots & a_{2n} \\
                   \hdotsfor{4} \\
                a_{n1} & a_{n2} & \cdots & a_{nn} \end{bmatrix},\quad
B=\begin{bmatrix} b_{11} & b_{12} & \cdots & b_{1n} \\
                b_{21} & b_{22} & \cdots & b_{2n} \\
                   \hdotsfor{4} \\
                b_{n1} & b_{n2} & \cdots & b_{nn} \end{bmatrix} \\
C=AB=\{c_{ij}\},\;c_{ij}=a_{i1}b_{1j}+a_{i2}b_{2j}+\dotsb+a_{in}b_{nj}
\end{gather*}
做一个$2n$级行列式
\[
D=\begin{vmatrix} a_{11} & a_{12} & \cdots & a_{1n}  & 0 & 0 & \cdots & 0\\
                a_{21} & a_{22} & \cdots & a_{2n}  & 0 & 0 & \cdots & 0 \\
                   \hdotsfor{8} \\
                a_{n1} & a_{n2} & \cdots & a_{nn}  & 0 & 0 & \cdots & 0 \\
                 -1 & 0 & \cdots & 0 & b_{11} & b_{12} & \cdots & b_{1n} \\
                 0 & -1 & \cdots & 0 & b_{21} & b_{22} & \cdots & b_{2n} \\
                   \hdotsfor{8} \\
                 0 & 0 & \cdots & -1 & b_{n1} & b_{n2} & \cdots & b_{nn} \end{vmatrix}
\]
根据拉普拉斯定义，将$D$按前$n$行展开，则因$D$中前$n$行除去左上角那个$n$级子式外，其余的$n$级子式都等于零。因此
\[
\det D=\det A \det B\]
对$D$作初等行变换，将第$n+1$行的$a_{11}$倍，第$n+2$行的$a_{12}$倍，$\dotsc$，第$2n$行的$a_{1n}$倍加到第一行，得
\[
D=\begin{vmatrix} 0 & 0 & \cdots & 0  & c_{11} & c_{12} & \cdots & c_{1n}\\
                a_{21} & a_{22} & \cdots & a_{2n}  & 0 & 0 & \cdots & 0 \\
                   \hdotsfor{8} \\
                a_{n1} & a_{n2} & \cdots & a_{nn}  & 0 & 0 & \cdots & 0 \\
                 -1 & 0 & \cdots & 0 & b_{11} & b_{12} & \cdots & b_{1n} \\
                 0 & -1 & \cdots & 0 & b_{21} & b_{22} & \cdots & b_{2n} \\
                   \hdotsfor{8} \\
                 0 & 0 & \cdots & -1 & b_{n1} & b_{n2} & \cdots & b_{nn} \end{vmatrix}
\]
再依此将第$n+1$行的$a_{k1}(k=2,3,\dotsc,n)$倍，第$n+2$行的$a_{k2}$倍，$\dotsc$，第$2n$行的$a_{kn}$倍加到第$k$行，就得
\[
D=\begin{vmatrix} 0 & 0 & \cdots & 0  & c_{11} & c_{12} & \cdots & c_{1n}\\
                0 & 0 & \cdots & 0  & c_{21} & c_{22} & \cdots & c_{2n} \\
                   \hdotsfor{8} \\
                0 & 0 & \cdots & 0  & c_{n1} & c_{n2} & \cdots & c_{nn} \\
                 -1 & 0 & \cdots & 0 & b_{11} & b_{12} & \cdots & b_{1n} \\
                 0 & -1 & \cdots & 0 & b_{21} & b_{22} & \cdots & b_{2n} \\
                   \hdotsfor{8} \\
                 0 & 0 & \cdots & -1 & b_{n1} & b_{n2} & \cdots & b_{nn} \end{vmatrix}
\]
由拉普拉斯定理
\begin{align*}
D&=(-1)^{n(n+1)+n^2}\begin{vmatrix} -1 & 0 & \cdots & 0\\
                   0 & -1 & \cdots & 0 \\
                   \hdotsfor{4} \\
                   0 & 0 & \cdots & -1 \\
                 \end{vmatrix}\begin{vmatrix}  c_{11} & c_{12} & \cdots & c_{1n}\\
                   c_{21} & c_{22} & \cdots & c_{2n} \\
                   \hdotsfor{4} \\
                   c_{n1} & c_{n2} & \cdots & c_{nn} \\
                 \end{vmatrix} \\
         &=\det C
\end{align*}
即$\det AB=\det A \det B$，定理得证。
\end{proof}
\begin{proof}
\[
\begin{bmatrix}
I & A \\ 0 & I
\end{bmatrix}
\begin{bmatrix}
A & 0 \\ -I & B
\end{bmatrix}=
\begin{bmatrix}
0 & AB \\ -I & B
\end{bmatrix}
\]
\end{proof}

\begin{quest}
\label{quest:78}
设
\[
A =
\begin{bmatrix}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{bmatrix}
\]
$A_{ij}$ 均为同阶矩阵，$A_{11}$与$A_{21}$乘法可换，$A_{11}$非奇异。
求证：
\[
\det{A} = \det \left( A_{11} A_{22} - A_{21} A_{12} \right)
\]
\end{quest}
\begin{proof}
由于
\begin{align*}
A &=
\begin{bmatrix}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{bmatrix} \\
&=\begin{bmatrix}
I & 0 \\
A_{21}A_{11}^{-1} &I
\end{bmatrix}
\begin{bmatrix}
A_{11} & 0 \\
0      & A_{22}-A_{21}A_{11}^{-1}A_{12}
\end{bmatrix}
\begin{bmatrix}
I & A_{11}^{-1}A_{12} \\
0 & I
\end{bmatrix}
\end{align*}
因此
\[
\begin{aligned}
\det A&= \begin{vmatrix}A_{11} & 0 \\
0      & A_{22}-A_{21}A_{11}^{-1}A_{12}
\end{vmatrix}\\
&=\det A_{11}\det (A_{22}-A_{21}A_{11}^{-1}A_{12})\\
&=\det A_{11}A_{22}-\det A_{21}A_{11}A_{11}^{-1}A_{12}\\
&=\det ( A_{11} A_{22} - A_{21} A_{12})
\end{aligned}
\]
\end{proof}

\begin{quest}
\label{quest:79}
设
\[
s_k = \lambda_{1}^k + \lambda_{2}^k + \dotsm + \lambda_{n}^k,\quad k = 1,2,\dotsc
\]
求证：
\[
\begin{vmatrix}
n        & s_1      & s_2    & \dotsm & s_{n-1}   \\
s_1      & s_2      & s_3    & \dotsm & s_{n}     \\
\hdotsfor{5}                                      \\
s_{n-1}  & s_{n}    & s_{n+1}& \dotsm & s_{2n-2}
\end{vmatrix}=
\prod_{1 \le j < i \le n} (\lambda_i - \lambda_j)^2
\]
\end{quest}
\begin{proof}
定义
\[
\Lambda \triangleq
\begin{bmatrix}
1               & 1               & 1               & \dotsm & 1                 \\
\lambda_1       & \lambda_2       & \lambda_3       & \dotsm & \lambda_{n}       \\
\lambda_1^2     & \lambda_2^2     & \lambda_3^2     & \dotsm & \lambda_{n}^2     \\
\hdotsfor{5}                                                                     \\
\lambda_1^{n-1} & \lambda_2^{n-1} & \lambda_3^{n-1} & \dotsm & \lambda_{n}^{n-1}
\end{bmatrix}
\]
其行列式为范德蒙\ (Vandermonde) 行列式，则有
\[ \det \Lambda = \prod_{1 \le j < i \le n} (\lambda_i - \lambda_j) \]
由于

\[
\Lambda \Lambda^T =
\begin{bmatrix}
n        & s_1      & s_2    & \dotsm & s_{n-1}   \\
s_1      & s_2      & s_3    & \dotsm & s_{n}     \\
\hdotsfor{5}                                      \\
s_{n-1}  & s_{n}    & s_{n+1}& \dotsm & s_{2n-2}
\end{bmatrix}
\]
因此
\[
\begin{vmatrix}
n        & s_1      & s_2    & \dotsm & s_{n-1}   \\
s_1      & s_2      & s_3    & \dotsm & s_{n}     \\
\hdotsfor{5}                                      \\
s_{n-1}  & s_{n}    & s_{n+1}& \dotsm & s_{2n-2}
\end{vmatrix}=(\det \Lambda )^2=
\prod_{1 \le j < i \le n} (\lambda_i - \lambda_j)^2
\]
\end{proof}

\begin{quest}
\label{quest:80}
\end{quest}

\begin{quest}
\label{quest:81}
\end{quest}

\begin{quest}
\label{quest:82}
\end{quest}

\begin{quest}
\label{quest:83}
\end{quest}

\begin{quest}
\label{quest:84}
\end{quest}

\begin{quest}
\label{quest:85}
\end{quest}

\begin{quest}[Lagrange 恒等式]
\label{quest:86}
求证：
\begin{enumerate}
\item
$\alpha_i,\beta_i\in\mathcal{R},i=1,2,\dotsc,n$
\[
\left(\sum_{i=1}^n\alpha_i^2\right)
\left(\sum_{i=1}^n\beta_i^2\right)-
\left(\sum_{i=1}^n\alpha_i\beta_i\right)^2=
\sum_{i<k}
\begin{vmatrix}
\alpha_i & \beta_i \\
\alpha_k & \beta_k
\end{vmatrix}^2
\]
\item
$\alpha_i,\beta_i\in\mathcal{C},i=1,2,\dotsc,n$
\[
\left(\sum_{i=1}^n\abs{\alpha_i}^2\right)
\left(\sum_{i=1}^n\abs{\beta_i}^2\right)-
\left|\sum_{i=1}^n\alpha_i\bar\beta_i\right|^2=
\left|\sum_{i<k}
\det
\begin{bmatrix}
\alpha_i & \beta_i \\
\alpha_k & \beta_k
\end{bmatrix}\right|^2
\]
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:87}
\end{quest}

\begin{quest}[Cauchy 不等式]
\label{quest:88}
求证：
\begin{enumerate}
\item
$\alpha_i,\beta_i\in\mathcal{R},i=1,2,\dotsc,n$
\[
\left(\sum_{i=1}^n\alpha_i\beta_i\right)^2
\leq
\left(\sum_{i=1}^n\alpha_i^2\right)
\left(\sum_{i=1}^n\beta_i^2\right)
\]
\item
$\alpha_i,\beta_i\in\mathcal{C},i=1,2,\dotsc,n$
\[
\left|\sum_{i=1}^n\alpha_i\bar\beta_i\right|^2
\leq
\left(\sum_{i=1}^n\abs{\alpha_i}^2\right)
\left(\sum_{i=1}^n\abs{\beta_i}^2\right)
\]
\item
一般地有
\[
\langle a, b \rangle^2
\leq
\langle a, a \rangle
\langle b, b \rangle
\]
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:89}
\end{quest}

\begin{quest}
\label{quest:90}
\end{quest}

\begin{quest}
\label{quest:91}
\end{quest}

\begin{quest}
\label{quest:92}
\end{quest}

\begin{quest}
\label{quest:93}
\end{quest}

\begin{quest}
\label{quest:94}
$n$ 阶方阵\ $A$ 的元素为\ $\pm1$，求证：
$\abs{A}$ 被\ $2^{n-1}$ 整除。
\end{quest}

\begin{quest}
\label{quest:95}
对实矩阵\ $A_{n\times n}=(\alpha_{ij})$，求证：
\[
\sup_{\abs{\alpha_{ij}}\leq1}\abs{\det A}\text{\ 被\ }2^{n-1}\text{\ 整除}
\]
\end{quest}

\begin{quest}
\label{quest:96}
\end{quest}

\begin{quest}
\label{quest:97}
$A=(\alpha_{ij})$, $B=(\beta_{ij})$ 均为\ $n$ 阶方阵，$\operatorname{rank}B\leq1$，
$\alpha_{ij}$ 在\ $\det A$ 中的代数余子式为\ $A_{ij}$，令\ $x=(\xi_1,\xi_2,\dotsc,\xi_n)^T$，
$y=(\eta_1,\eta_2,\dotsc,\eta_n)^T$，求证：
\begin{enumerate}
\item
\[
\abs{A+B}=\abs{A}+\sum_{i,j=1}^n\beta_{ij}A_{ij}
\]
\item
\[
\abs{A+xy^T}=\abs{A}+\sum_{i,j=1}^n\xi_i\eta_jA_{ij}=\abs{A}+y^TA^*x
\]
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:98}
已知\ $n$ 个\ $n$ 元函数：$y_i=x_i/r,i=1,2,\dotsc,n$，其中\ $r=\sum_{k=1}^nx_k^2$，
$J=(\partial y_i/\partial x_j)$ 为\ Jacobi 矩阵。求证：
\[
\abs{J}=-r^{-n}
\]
\end{quest}

\begin{quest}
\label{quest:99}
求下列$n$阶行列式的值：
\[
\begin{vmatrix}
\alpha          & \beta           & \beta           & \cdots & \beta             \\
\beta           & \alpha          & \beta           & \cdots & \beta             \\
\beta           & \beta           & \alpha          & \cdots & \beta             \\
\cdots          & \cdots          & \cdots          & \cdots & \cdots            \\
\beta           & \beta           & \beta           & \cdots & \alpha
\end{vmatrix}
\]
\end{quest}

\begin{quest}
\label{quest:100}
设
\[
A(\lambda)=
\begin{vmatrix}
\alpha_{11}+\lambda & \alpha_{12}+\lambda & \cdots & \alpha_{1n}+\lambda \\
\alpha_{21}+\lambda & \alpha_{22}+\lambda & \cdots & \alpha_{2n}+\lambda \\
\hdotsfor{4}                                                             \\
\alpha_{n1}+\lambda & \alpha_{n2}+\lambda & \cdots & \alpha_{nn}+\lambda
\end{vmatrix}
\]
求证：
\[
A(\lambda)=\abs{A}+\lambda\sum_{i,j=1}^nA_{ij}
\]
其中\ $A_{ij}$ 为\ $\alpha_{ij}$ 在\ $\abs{A}$ 中的代数余子式。
\end{quest}

\begin{quest}
\label{quest:101}
$A=(\alpha_{ij})$，$A_{ij}$ 为\ $\alpha_{ij}$ 在\ $\abs{A}$ 中的代数余子式，求证：
\[
\sum_{i,j=1}^nA_{ij}=
\begin{vmatrix}
\alpha_{11}-\alpha_{12} & \alpha_{12}-\alpha_{13} & \cdots & \alpha_{1,n-1}-\alpha_{1n} & 1 \\
\alpha_{21}-\alpha_{22} & \alpha_{22}-\alpha_{23} & \cdots & \alpha_{2,n-1}-\alpha_{2n} & 1 \\
\hdotsfor{5}                                                                                \\
\alpha_{n1}-\alpha_{n2} & \alpha_{n2}-\alpha_{n3} & \cdots & \alpha_{n,n-1}-\alpha_{nn} & 1
\end{vmatrix}
\]
\end{quest}

\begin{quest}
\label{quest:102}
求证：
\[
\begin{split}
&
\begin{vmatrix}
\alpha_{11}+\alpha_{12}+\dotsb+\alpha_{1,n-1} &
\alpha_{12}+\alpha_{13}+\dotsb+\alpha_{1n}    &
\cdots &
\alpha_{11}+\alpha_{12}+\dotsb+\alpha_{1,n-2}+\alpha_{1n} \\
\alpha_{21}+\alpha_{22}+\dotsb+\alpha_{2,n-1} &
\alpha_{22}+\alpha_{23}+\dotsb+\alpha_{2n}    &
\cdots &
\alpha_{21}+\alpha_{22}+\dotsb+\alpha_{2,n-2}+\alpha_{2n} \\
\hdotsfor{4} \\
\alpha_{n1}+\alpha_{n2}+\dotsb+\alpha_{n,n-1} &
\alpha_{n2}+\alpha_{n3}+\dotsb+\alpha_{nn}    &
\cdots &
\alpha_{n1}+\alpha_{n2}+\dotsb+\alpha_{n,n-2}+\alpha_{nn}
\end{vmatrix}\\
=&(n-1)\abs{A}
\end{split}
\]
\end{quest}

\begin{quest}
\label{quest:103}
求下列\ $n$ 阶行列式的值：
\[
\begin{vmatrix}
2n              & n               &                 &        &                   \\
n               & 2n              & n               &        &                   \\
                & \ddots          & \ddots          & \ddots &                   \\
                &                 & n               & 2n     & n                 \\
                &                 &                 & n      & 2n
\end{vmatrix}
\]
\end{quest}
\begin{proof}
\[
D_{n} \triangleq
\begin{vmatrix}
2               & 1               &                 &        &                   \\
1               & 2               & 1               &        &                   \\
                & \ddots          & \ddots          & \ddots &                   \\
                &                 & 1               & 2      & 1                 \\
                &                 &                 & 1      & 2
\end{vmatrix}
\]
则有
\[
D_{n} = 2 D_{n-1} - D_{n-2}
\]
即
\[
D_{n} - D_{n-1} = D_{n-1} - D_{n-2} = \dotsm = D_{2} - D_{1} = 1
\]
得
\[
D_{n} = n - 1 + D_{1} = n + 1
\]
可知
\begin{align*}
\begin{vmatrix}
2n              & n               &                 &        &                   \\
n               & 2n              & n               &        &                   \\
                & \ddots          & \ddots          & \ddots &                   \\
                &                 & n               & 2n     & n                 \\
                &                 &                 & n      & 2n
\end{vmatrix}
&=n^n
\begin{vmatrix}
2               & 1               &                 &        &                   \\
1               & 2               & 1               &        &                   \\
                & \ddots          & \ddots          & \ddots &                   \\
                &                 & 1               & 2      & 1                 \\
                &                 &                 & 1      & 2
\end{vmatrix}\\
&=
n^n D_n = n^n (n + 1)
\end{align*}
\end{proof}

\begin{quest}
\label{quest:104}
已知\ $AX=B$，求\ $X$。其中\ $A_{n \times n}$、$B_{n \times n}$ 为：
\[
A=
\begin{bmatrix}
1               & 1               & 1               & \cdots & 1                 \\
0               & 1               & 1               & \cdots & 1                 \\
0               & 0               & 1               & \cdots & 1                 \\
\hdotsfor{5}                                                                     \\
0               & 0               & 0               & \cdots & 1
\end{bmatrix}
\quad
B=
\begin{bmatrix}
1               & 2               & 3               & \cdots & n                 \\
0               & 1               & 2               & \cdots & n-1               \\
0               & 0               & 1               & \cdots & n-2               \\
\hdotsfor{5}                                                                     \\
0               & 0               & 0               & \cdots & 1
\end{bmatrix}
\]
\end{quest}
\begin{proof}
\begin{align*}
X&=A^{-1}B=\frac{1}{\det A}A^*B \\ &=\begin{bmatrix}
1               & -1               & 0               & \cdots & 0                 \\
0               & 1                & -1              & \cdots & 0                \\
0               & 0                & 1               & \cdots & 0                 \\
\hdotsfor{5}                                                                     \\
0               & 0               & 0               & \cdots & 1
\end{bmatrix}\begin{bmatrix}
1               & 2               & 3               & \cdots & n                 \\
0               & 1               & 2               & \cdots & n-1               \\
0               & 0               & 1               & \cdots & n-2               \\
\hdotsfor{5}                                                                     \\
0               & 0               & 0               & \cdots & 1
\end{bmatrix} \\ &=\begin{bmatrix}
1               & 1               & 1               & \cdots & 1                 \\
0               & 1               & 1               & \cdots & 1                 \\
0               & 0               & 1               & \cdots & 1                 \\
\hdotsfor{5}                                                                     \\
0               & 0               & 0               & \cdots & 1
\end{bmatrix}\\&=A
\end{align*}
\end{proof}

\begin{quest}
\label{quest:105}
证明\ Fibonacci 数列满足：$F_1=1,F_2=2,F_n=F_{n-1}+F_{n-2}(n \ge 3)$，其中
\[
F_n=
\begin{vmatrix}
1               & 1               &                 &        &                   \\
-1              & 1               & 1               &        &                   \\
                & \ddots          & \ddots          & \ddots &                   \\
                &                 & -1              & 1      & 1                 \\
                &                 &                 & -1     & 1
\end{vmatrix}
\]
\end{quest}
\begin{proof}
易证
\[
F_1=1, \quad
F_2=\begin{vmatrix} 1 & 1 \\-1 & 1 \end{vmatrix}=2
\]
定义$(n-1)$阶矩阵
\[
A_{n-1} \triangleq \begin{bmatrix}
1               & 1               &                 &        &                   \\
-1              & 1               & 1               &        &                   \\
                & \ddots          & \ddots          & \ddots &                   \\
                &                 & -1              & 1      & 1                 \\
                &                 &                 & -1     & 1
\end{bmatrix},\; n \ge 3
\]
则
\begin{align*}
F_n&=F_{n-1}\left(1-\frac{1}{F_{n-1}}\begin{bmatrix} 0 & \cdots & 0 & -1 \end{bmatrix} A_{n-1}^* \begin{bmatrix}0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}\right) \\
   &=F_{n-1}\left(1+\frac{F_{n-2}}{F_{n-1}}\right) \\
   &=F_{n-1}+F_{n-2}
\end{align*}
\end{proof}

\begin{quest}
\label{quest:106}
设\/ $\alpha$, $\beta$, $\gamma$ 是方程\/ $x^3+px+q=0$ 的根，求行列式值：
\[
\begin{vmatrix}
\alpha & \beta  & \gamma \\
\gamma & \alpha & \beta  \\
\beta  & \gamma & \alpha
\end{vmatrix}
\]
\end{quest}
\begin{proof}
$ $

$\alpha$, $\beta$, $\gamma$ 是方程\/ $x^3+px+q=0$ 的根，
则由韦达定理有
\[
\alpha + \beta + \gamma = 0,\quad \alpha \beta \gamma = -q
\]
由
\begin{align*}
\alpha^3 + p \alpha + q = 0 \\
\beta^3  + p \beta  + q = 0 \\
\gamma^3 + p \gamma + q = 0
\end{align*}
将以上三式相加，得
\[
\alpha^3 + \beta^3 + \gamma^3 + p(\alpha + \beta + \gamma) + 3 q = 0
\]
即
\[
\alpha^3 + \beta^3 + \gamma^3 -3 \alpha \beta \gamma = 0
\]
则有
\[
\begin{vmatrix}
\alpha & \beta  & \gamma \\
\gamma & \alpha & \beta  \\
\beta  & \gamma & \alpha
\end{vmatrix}
=
\alpha^3+\beta^3+\gamma^3-3\alpha \beta \gamma
=
0
\]
\end{proof}

\begin{quest}
\label{quest:107}
已知三阶行列式中有两个元素为\ $4$，其余为\ $\pm1$，
求证：这样的三阶行列式的最大值为\ $25$，并求出该行列式。
\end{quest}

\begin{quest}
\label{quest:108}
求证：
\begin{enumerate}
\item
$n$ 阶行列式的\ $n!$ 项中，有且仅有一项为次对角元元素的乘积，其余项中则至少各有一个因子是
次对角线左上方与右下方的元素；
\item
$n$ 为奇数时，下列行列式非零：
\[
\begin{vmatrix}
1               & 2               & 3               & \cdots & n-1       & n                 \\
2^2             & 3^2             & 4^2             & \cdots & n^2       & (n+1)^2           \\
3^3             & 4^3             & 5^3             & \cdots & (n+1)^3   & (n+1)^3           \\
\hdotsfor{6}                                                                                 \\
n^n             & (n+1)^n         & (n+1)^n         & \cdots & (n+1)^n   & (n+1)^n
\end{vmatrix}
\]
\end{enumerate}
\end{quest}

\begin{quest}[Sherman-Morrison 公式]
\label{quest:109}
$A$ 非异，$u, v$ 为向量，$v^TA^{-1}u+1\ne0$，求证：$A+uv^T$ 非异，且
\[
(A+uv^T)^{-1}=A^{-1}-\frac{A^{-1}uv^TA^{-1}}{1+v^TA^{-1}u}
\]
\end{quest}
\begin{proof}
由于
\begin{equation}
\label{equ:schur}
\begin{aligned}
\begin{bmatrix} 1 & -v^T \\ u & A \end{bmatrix}&=
\begin{bmatrix} I & 0 \\ u & I \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & A+uv^T  \end{bmatrix}
\begin{bmatrix} I & -v^T \\ 0 & I \end{bmatrix} \\
&=\begin{bmatrix} I & -v^TA^{-1} \\ 0 & I \end{bmatrix}\begin{bmatrix} 1+v^TA^{-1}u & 0 \\ 0 & A  \end{bmatrix}
\begin{bmatrix} I & 0\\ A^{-1}u & I \end{bmatrix}
\end{aligned}
\end{equation}
因此
\[
\det (A+uv^T)=  (1+v^TA^{-1}u)\det A \neq 0
\]
由 \equref{equ:schur},
\begin{align*}
\begin{bmatrix} 1 & 0 \\ 0 & A+uv^T  \end{bmatrix}^{-1}&=
\begin{bmatrix} I & -v^T \\ 0 & I \end{bmatrix}\begin{bmatrix} I & 0\\ A^{-1}u & I \end{bmatrix}^{-1}
\begin{bmatrix} 1+v^TA^{-1}u & 0 \\ 0 & A  \end{bmatrix}^{-1}\begin{bmatrix} I & -v^TA^{-1} \\ 0 & I \end{bmatrix}^{-1}
\begin{bmatrix} I & 0 \\ u & I \end{bmatrix} \\
&=\begin{bmatrix} I & -v^T \\ 0 & I \end{bmatrix}\begin{bmatrix} I & 0\\ -A^{-1}u & I \end{bmatrix}
\begin{bmatrix} (1+v^TA^{-1}u)^{-1} & 0 \\ 0 & A^{-1}  \end{bmatrix}\begin{bmatrix} I & v^TA^{-1} \\ 0 & I \end{bmatrix}
\begin{bmatrix} I & 0 \\ u & I \end{bmatrix}\\
&=\begin{bmatrix}1 & 0 \\ 0 &A^{-1}-A^{-1}u (1+v^TA^{-1}u)^{-1}v^TA^{-1}  \end{bmatrix}
\end{align*}
可得
\[
(A+uv^T)^{-1}=A^{-1}-\frac{A^{-1}uv^TA^{-1}}{1+v^TA^{-1}u}
\]
\end{proof}

\begin{quest}
\label{quest:110}
设$A,B$为同阶实方阵，求证：
\begin{enumerate}
\item
\[
\begin{vmatrix}
A & B \\
B & A
\end{vmatrix}=
\begin{vmatrix} A + B \end{vmatrix}
\begin{vmatrix} A - B \end{vmatrix}
\]
\item
\[
\begin{vmatrix}
A & -B \\
B & A
\end{vmatrix}=
\abs{\det(A + i B)}^2
\]
\end{enumerate}
\end{quest}
\begin{proof}
$ $

\begin{enumerate}
\item
\begin{align*}
\begin{vmatrix}
A & B \\
B & A
\end{vmatrix}
&=
\begin{vmatrix}
A+B & B \\
B+A & A
\end{vmatrix}
=
\begin{vmatrix} A+B & B \\ 0 & A-B \end{vmatrix} \\
&=
{\color{red}
\begin{vmatrix}
\begin{pmatrix} I & 0 \\ -I & I \end{pmatrix}
\begin{pmatrix} A & B \\ B & A \end{pmatrix}
\begin{pmatrix} I & 0 \\ I & I \end{pmatrix}
\end{vmatrix}} \\
&=
\begin{vmatrix} A+B & B \\ 0 & A-B \end{vmatrix} \\
&=
\abs{A + B}\abs{A-B}
\end{align*}
\item
\begin{align*}
\begin{vmatrix}
A & -B \\
B & A
\end{vmatrix}&=\frac{1}{i}\begin{vmatrix}
A & -B \\
iB & iA
\end{vmatrix} \\
&=
\frac{1}{i}\begin{vmatrix}
A+iB & iA-B \\
iB & iA
\end{vmatrix}\\
&=-\frac{1}{i^2}\begin{vmatrix}
A+iB & A+iB \\
iB & A
\end{vmatrix}\\
&=
\begin{vmatrix}A+iB & 0 \\
iB & A-iB
\end{vmatrix} \\
&=
{\color{red}
\begin{vmatrix}
\begin{pmatrix} I & i I \\ 0 & i I \end{pmatrix}
\begin{pmatrix} A & -B \\ B & A \end{pmatrix}
\begin{pmatrix} I & - I \\ 0 & - i I \end{pmatrix}
\end{vmatrix}} \\
&=
{\color{red}\det(A + iB)(A-iB)} \\
&=
\det(A + iB)(\overline{A+iB}) \\
&=
\det(A + iB)\,\det(\overline{A+iB}) \\
&=
\det(A + iB)\,\overline{\det(A+iB)} \\
&= \abs{\det(A + i B)}^2
\end{align*}
\end{enumerate}
\end{proof}

%\section{线性空间}
%\char"48o\char'167{ }\char"61r\char"65\ \char"79o\char117\char'77

\begin{quest}
\label{quest:111}
向量组\ $a_1, a_2,\dots,a_k$\ 满足下列条件之一者，必线性相关：
\begin{enumerate}
\item
某一个\ $a_i = 0, 1 \leq i \leq k$；
\item
某两个向量成比例，即有\ $a_i = \lambda a_j, 1 \leq i, j \leq k$；
\item
部分向量线性相关。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:112}
$k$ 元向量组
\[
a_j =
\begin{bmatrix}
a_{1j} & a_{2j} & \cdots & a_{kj}
\end{bmatrix}^T,\quad l=1,2,\dotsc,s
\]
求证：
\begin{enumerate}
\item
如果\ $a_j$ 线性无关，则把每个向量加长以后形成的新向量仍然线性无关；
\item
如果\ $a_j$ 线性相关，则由某部分分量形成的新向量仍然线性相关。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:113}
证明线性表出的传递性。
\end{quest}

\begin{quest}
\label{quest:114}
向量组\ $a_1, a_2,\dots,a_n$\ 的秩为\ $s$，则加入向量\ $y$\ 后秩最多增加\ $1$。
且秩仍为\ $s$\ 的充要条件为\ $y$\ 可用\ $a_1, a_2,\dots,a_n$\ 线性表出。
\end{quest}
\begin{proof}
分两种情况判断：
\begin{enumerate}
\item
$y$\ 可用\ $a_1, a_2,\dots,a_n$\ 线性表出\ $\Longrightarrow$\ 秩不变；
\item
$y$\ 不能用\ $a_1, a_2,\dots,a_n$\ 线性表出\ $\Longrightarrow$\ 极大线性无关组中可加入\ $y$\ $\Longrightarrow$\ 秩增加\ $1$。
\end{enumerate}
即秩最多增加\ $1$。

充分条件显然，必要条件可用反证法证出。
\end{proof}

\begin{quest}
\label{quest:115}
矩阵\ $A$\ 的列向量线性无关的充要条件为\ $\det{A} \neq 0$。
\end{quest}
\begin{proof}
考虑方程\ $Ax=0$ 仅有零解\ $\Longleftrightarrow \det{A} \neq 0$
\end{proof}

\begin{quest}
\label{quest:116}
设\ $\lambda_1,\lambda_2,\dots,\lambda_{n}$ 各不相同，求证：
\[
x_i =
\begin{bmatrix}
1 & \lambda_i & \cdots & \lambda_i^{n-1}
\end{bmatrix}^T,\quad i=1,2,\dotsc,n
\]
线性无关。
\end{quest}

\begin{quest}
\label{quest:117}
设向量组
\[
a_1, a_2,\dots,a_s
\]
的秩为\ $r$，证：
\begin{enumerate}
\item
其中任意\ $r$ 个线性无关的向量都构成它的一个极大线性无关组；
\item
当每一个向量都可用其中某\ $r$ 个向量线性表出时，这\ $r$ 个向量就是它的一个极大线性无关组。
\end{enumerate}
\end{quest}
\begin{proof}
$ $

\begin{enumerate}
\item
考虑再加入一个向量后的向量组必线性相关，否则和秩为\ $r$ 矛盾；
\item
如果这\ $r$ 个向量是线性相关的，则存在一组数目小于\ $r$ 的向量构成其极大线性无关组，从而推出矛盾。
\end{enumerate}
\end{proof}

\begin{quest}
\label{quest:118}
向量\ $b$ 可用向量组\ $a_1, a_2,\dots,a_s$ 线性表出，
求证：此向量组线性无关的充要条件为表示法唯一。
\end{quest}

\begin{quest}
\label{quest:119}
设向量组
\[
a_1, a_2,\dots,a_r
\]
线性无关，又有
\[
b_i = \sum_{j=1}^{r} \beta_{ij} a_j, \quad i = 1,2,\dots,s
\]
求证：
\begin{enumerate}
\item
向量组\ $b_1,b_2,\dots,b_s$ 的秩等于\ $B \triangleq (\beta_{ij})$ 的秩；
\item
当\ $s=r$ 时，$b_1,b_2,\dots,b_s$ 线性无关的充要条件为\ $\det B \neq 0$。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:120}
求证：$a_1, a_2,\dots,a_s$ (其中\ $a_1 \neq 0$)线性无关的充要条件是至少
有一个\ $a_k(1 < k \leq s)$ 可用\ $a_1, a_2,\dots,a_{k-1}$ 线性表出。
\end{quest}

\begin{quest}
\label{quest:121}
$a$ 可用\ $b,c_1,c_2,\dots,c_s$ 线性表出，且表示式中\ $b$ 的系数不为\ $0$，求证：
向量组\ $I$: $a,c_1,c_2,\dots,c_s$ 与
向量组\ $II$: $b,c_1,c_2,\dots,c_s$ 等价。
\end{quest}

\begin{quest}[Steinitz 替换定理]
\label{quest:122}
向量组\ $I$
\[
a_1, a_2,\dots,a_s
\]
和向量组\ $II$
\[
b_1, b_2,\dots,b_r
\]
$II$ 可由\ $I$ 线性表出，则
\[
s < r \Longrightarrow II \text{线性相关}
\]
\end{quest}

\begin{quest}
\label{quest:123}
向量组\ $I$: $b_1,b_2,\dots,b_t$ 可用
向量组\ $II$: $a_1,a_2,\dots,a_k$ 线性表出，
组\ $I$ 与组\ $II$ 的秩分别为\ $r$ 与\ $s$，求证：$r \leq s$
\end{quest}

\begin{quest}
\label{quest:124}
求证：两向量组等价的必要条件为秩相等。
\end{quest}

\begin{quest}
\label{quest:125}
$ $

\begin{enumerate}
\item
向量组\ $I$ 与向量组\ $II$ 的个数相等且彼此等价，
求证：组\ $I$ 线性无关的充要条件为组\ $II$ 线性无关。
\item
求证：$n$ 维空间\ $V$ 中任意\ $n$ 个向量线性无关的充要条件为一组已知的基
(或\ $V$ 中任一向量)可用这\ $n$ 个向量线性表出。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:126}
设向量组\ $I$ 与\ $II$ 的秩均为\ $r$，且\ $I$ 可由\ $II$ 线性表出。证：$I$ 与\ $II$ 等价。
\end{quest}
\begin{proof}
$ $

设\ $I$ 与\ $II$ 的一个极大线性无关组为
\[
a_1, a_2,\dots,a_r
\]
和
\[
b_1, b_2,\dots,b_r
\]
由假设有\ $a_1, a_2,\dots,a_r$ 可由\ $b_1, b_2,\dots,b_r$ 线性表出，
所以对于\ $\forall c \in II$，$a_1, a_2,\dots,a_r,c$ 也可由\ $b_1, b_2,\dots,b_r$ 线性表出。
由\ Steinitz 替换定理可知，$a_1, a_2,\dots,a_r,c$ 必线性相关。
考虑到\ $a_1, a_2,\dots,a_r$ 线性无关，则\ $c$ 一定可由\ $a_1, a_2,\dots,a_r$ 线性表出，即\ $II$ 亦可由\ $I$ 线性表出，
则可知\ $I$ 与\ $II$ 等价。
\end{proof}

\begin{quest}
\label{quest:127}
求证：一个含有有限个向量的向量组\ $I$，或者有限维线性空间中的任意多个向量的向量组，
从任一个线性无关组，均可扩充成为(该向量组的)一个极大线性无关组。
\end{quest}

\begin{quest}
\label{quest:128}
向量组\ $I$: $b_1,b_2,\dots,b_m$ 线性无关，
且可用向量组\ $II$: $a_1,a_2,\dots,a_l$ 线性表出，
求证：一定存在一个正整数\ $k$($1\leq k\leq l$)，
使\ $a_k,b_2,\dots,b_m$ 线性无关。
\end{quest}

\begin{quest}
\label{quest:129}
$A$, $B$ 为\ $n \times n$ 非奇异矩阵，
列向量为\ $a_i$, $b_i$, $i=1,2,\dotsc,n$, 求证：
在适当调整\ $A$ 的列向量次序之后，以下矩阵均非奇异：
\[
A_l =
\begin{bmatrix}
a_1 & a_2 & \cdots & a_l & b_{l+1} & \cdots & b_n
\end{bmatrix},\quad l=1,2,\dotsc,n
\]
\end{quest}

\begin{quest}
\label{quest:130}
$A$ 为分块对角矩阵：
\[
A = \operatorname{diag} (A_1,A_2,\dotsc,A_k)
\]
求证：
\[
\operatorname{rank} A =
\operatorname{rank} A_1 +
\operatorname{rank} A_2 + \dotsb +
\operatorname{rank} A_k
\]
\end{quest}

\begin{quest}
\label{quest:131}
向量组\ $I$: $a_1,a_2,\dots,a_r$ 与
向量组\ $II$: $a_1,a_2,\dots,a_r,a_{r+1},\dots,a_s$ 有相同的秩，
求证：$I$ 与\ $II$ 等价。
\end{quest}

\begin{quest}
\label{quest:132}
\[
\begin{split}
b_1 &= a_2 + a_3 + \dotsb + a_r     \\
b_2 &= a_1 + a_3 + \dotsb + a_r     \\
    &\vdots                         \\
b_r &= a_1 + a_2 + \dotsb + a_{r-1}
\end{split}
\]
求证：
向量组\ $I$: $b_1,b_2,\dots,b_r$ 与
向量组\ $II$: $a_1,a_2,\dots,a_r$ 有相同的秩。
\end{quest}

\begin{quest}
\label{quest:133}
求证：
\[
\operatorname{rank} (AB) \leq \min (\operatorname{rank} A,\operatorname{rank} B)
\]
\end{quest}

\begin{quest}
\label{quest:134}
求证：用非奇异矩阵左乘(或右乘)不改变原来矩阵的秩。
\end{quest}

\begin{quest}
\label{quest:135}
$ $

\begin{enumerate}
\item
设向量组\ $a_1,a_2,\dots,a_n$ 的秩为\ $r$，
求证：从中任意取出\ $s$ 个向量形成的新向量组的秩为\ $t$，则有
\[
t \geq r + s -n
\]
\item
设\ $\operatorname{rank} A_{n \times k} = r$，
在\ $A$ 中任取\ $s$ 行形成矩阵\ $A_1$，
求证：
\[
\operatorname{rank} A_1 \geq r + s -n
\]
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:136}
设\ $\operatorname{rank} A_{n \times k} = r$，
在\ $A$ 中任取\ $s$ 行和\ $t$ 列形成矩阵\ $C_{s \times t}$，
求证：
\[
\operatorname{rank} C \geq r + s + t - n - k
\]
\end{quest}

\begin{quest}
\label{quest:137}
设\ $C = (A,B)$，求证：
\[
\operatorname{rank} C \leq \operatorname{rank} A + \operatorname{rank} B
\]
\end{quest}

\begin{quest}
\label{quest:138}
设有向量组\ $I$: $a_1,a_2,\dots,a_s$；
$II$: $b_1,b_2,\dots,b_t$ 和\ $III$: $a_1,a_2,\dots,a_s,b_1,b_2,\dots,b_t$，
秩各为\ $r_{I}$, $r_{II}$, $r_{III}$，求证：
\[
\max (r_{I},r_{II}) \leq r_{III} \leq r_{I} + r_{II}
\]
\end{quest}

\begin{quest}
\label{quest:139}
求证：
\[
\operatorname{rank} ( A \pm B ) \leq \operatorname{rank} A + \operatorname{rank} B
\]
\end{quest}

\begin{quest}
\label{quest:140}
求证：
\[
\abs{\operatorname{rank} A - \operatorname{rank} B}
\leq
\operatorname{rank} ( A \pm B )
\]
\end{quest}

\begin{quest}
\label{quest:141}
设\ $A$ 为方阵，多项式\ $f(\lambda)$ 满足\ $f(0)=0$，
求证：
\[
\operatorname{rank} f(A)
\leq
\operatorname{rank} A
\]
\end{quest}

\begin{quest}
\label{quest:142}
设\ $\operatorname{rank} A_{n \times k}=s$，
$\operatorname{rank} B_{k \times m}=t$，
求证：
\[
\operatorname{rank} A B
\geq
s + t - k
\]
\end{quest}

\begin{quest}
\label{quest:143}
求证：
\[
\operatorname{rank} A B C
\geq
\operatorname{rank} A B +
\operatorname{rank} B C -
\operatorname{rank} B
\]
\end{quest}

\begin{quest}
\label{quest:144}
设\ $A$, $B$ 均为\ $n$ 阶矩阵，且\ $AB=0$，
求证：
\[
\operatorname{rank} A +
\operatorname{rank} B
\leq n
\]
\end{quest}

\begin{quest}
\label{quest:145}
设\ $A\neq 0$，
如果存在非零矩阵\ $B$ 使\ $AB=0$，则称\ $A$ 为左零因子，
类似地，
若存在非零矩阵\ $C$ 使\ $CA=0$，则称\ $A$ 为右零因子。
求证：
$A_{n \times k}$ 为左(右)零因子的充要条件为
\[
\operatorname{rank} A \leq k
\text{(}
\operatorname{rank} A \leq n
\text{)}
\]
\end{quest}

\begin{quest}
\label{quest:146}
$A$ 为实矩阵，求证：
\begin{enumerate}
\item
$A^T A x = 0$ 充要条件为\ $Ax=0$ ($A$ 为复矩阵时，则为\ $A^H A x = 0 \Longleftrightarrow Ax=0$)
\item
$\operatorname{rank}A^TA=\operatorname{rank}A=\operatorname{rank}AA^T$
($A$ 为复矩阵时，
则为\ $\operatorname{rank}A^HA=\operatorname{rank}A=\operatorname{rank}AA^H$)
\item
$A$ 列无关的充要条件为\ $A^T A$($A^H A$) 非奇异。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:147}
求证：
\begin{enumerate}
\item
$A_{n \times k}(k < n)$ 列线性无关的充要条件为存在\ $B_{n \times (n-k)}$ 列线性无关，
使\ $P=(A,B)$ 非奇异
\item
$A_{n \times k}(n < k)$ 行线性无关的充要条件为存在\ $B_{(k - n) \times k}$ 行线性无关，
使\ $P=(A;B)$ 非奇异
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:148}
若\ $B_{k \times n} A_{n \times k} = I_k$，则称\ $B$ 为\ $A$ 的左逆(或\ $A$ 为\ $B$ 的右逆)，证：
\begin{enumerate}
\item
矩阵\ $A$ 为列(行)线性无关的充要条件为存在左(右)逆；
\item
矩阵\ $A$ 左(右)逆唯一的充要条件为\ $A$ 为行(列)线性无关，即\ $A$ 非奇异。
\end{enumerate}
\end{quest}
\begin{proof}
$ $

\begin{enumerate}
\item
\begin{description}
\item[$\Longrightarrow$]
矩阵\ $A$ 列线性无关，则\ $A^T A$ 非奇异，可构造矩阵\ $B = (A^T A)^{-1} A^T$，易证
\[
B A = (A^T A)^{-1} A^T A = I
\]
\item[$\Longleftarrow$]
左逆存在，即存在\ $B A = I$。设\ $A x = 0$，则有
\[
B A x = I x = x = 0
\]
即矩阵\ $A$ 列线性无关。
\end{description}
\item
\[
\begin{split}
& B_1 A = I, B_2 A = I \Longrightarrow B_1 = B_2 \\
\Longleftrightarrow & \forall B: B A = 0 \Longrightarrow B = 0 \\
\Longleftrightarrow & A \text{ 行无关}
\end{split}
\]
\end{enumerate}
\end{proof}

\begin{quest}
\label{quest:149}
$A_{n \times k}$ 列线性无关，$k<n$，求证：
\begin{enumerate}
\item
存在\ $B_{n \times (n-k)}$ 列线性无关，使\ $B^T A=0$ 且\ $P=(A,B)$ 非奇异
\item
若存在\ $A^TC=0$，$C$ 的列数\ $s>n-k$，则\ $C$ 必列线性相关
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:150}
$ $

\begin{enumerate}
\item
设\ $B$ 与\ $C$ 均列线性无关，则对任何维数相容矩阵\ $A$ 有
\[
\operatorname{rank} A = \operatorname{rank} B A = \operatorname{rank} A C^T = \operatorname{rank} B A C^T
\]
即以列(行)无关矩阵左(右)乘不改变原矩阵的秩。
\item
设矩阵\ $A$ 行无关，证：
$ \operatorname{rank} A = \operatorname{rank} B A \Longleftrightarrow $\ $B$ 列无关。
\end{enumerate}
\end{quest}
\begin{proof}
$ $

\begin{enumerate}
\item
由{\questref{quest:133}} 可得：
$\operatorname{rank} B A \leq \min ( \operatorname{rank} A, \operatorname{rank} B) \leq \operatorname{rank} A$。

已知\ $B$ 列线性无关，则由{\questref{quest:148}} 可知存在左逆\ $B^{*}$ 满足\ $B^{*} B = I$。
由{\questref{quest:133}} 可得：
$\operatorname{rank} B^{*} B A \leq \min ( \operatorname{rank} B^{*}, \operatorname{rank} B A) \leq \operatorname{rank} B A$，
即\ $\operatorname{rank} A \leq \operatorname{rank} B A$。

综合以上推导有\ $\operatorname{rank} A = \operatorname{rank} B A$。
\item
\begin{description}
\item[$\Longrightarrow$]
矩阵\ $A$ 行无关，则有\ $\operatorname{rank} B = \operatorname{rank} B A $，
即\ $\operatorname{rank} B = \operatorname{rank} A = A \text{ 的行数}$，
而矩阵\ $A$ 的行数与矩阵\ $B$ 的列数相等，
即\ $\operatorname{rank} B = B \text{ 的列数} \Longrightarrow B \text{ 列无关}$。
\item[$\Longleftarrow$]
直接引用第一个问题的结论即可证。
\end{description}
\end{enumerate}
\end{proof}

\begin{quest}
\label{quest:151}
求证：{\questref{quest:30}} 逆命题成立，即
\[
\operatorname{rank}A_{n\times k}=r
\Longleftrightarrow
\exists B_{n\times r},C_{k\times r}:
\operatorname{rank}B=\operatorname{rank}C=r,
A=BC^T
\]
\end{quest}

\begin{quest}
\label{quest:152}
求证：
\begin{enumerate}
\item
$A_{n\times r}$ 列线性无关的充要条件为\ $A=B_{n\times r}D_{r\times r}$，
其中\ $B$ 列线性无关，$D$ 非奇异。
\item
如果又有\ $A=B_1D_1$，其中\ $B_1$ 列线性无关，$D_1$ 非奇异，
则存在非奇异矩阵\ $P$ 使：$B P = B_1$, $P^{-1} D = D_1$
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:153}
设矩阵\ $A$ 的列线性无关分解为：$A = B C^T$，其中\ $B, C$ 列线性无关。
证：对任意两组分解\ $B_1, C_1$ 和\ $B_2, C_2$，存在非奇异矩阵\ $P$ 满足：
$B_1 P = B_2, P^{-1} C_1^T = C_2^T$。
\end{quest}
\begin{proof}
已知
\[
A = B_1 C_1^T = B_2 C_2^T
\]
且\ $B_1, C_1$ 和\ $B_2, C_2$ 列线性无关，则存在\ $M_1, N_1$ 和\ $M_2, N_2$ 满足：
\[
M_1 B_1 = M_2 B_2 = N_1 C_1 = N_2 C_2 = I
\]
定义\ $P \triangleq M_1 B_2$，则有
\[
\begin{split}
I
&= M_1 B_1 (N_1 C_1)^T \\
&= M_1 B_1 C_1^T N_1^T \\
&= M_1 B_2 C_2^T N_1^T \\
&= P C_2^T N_1^T
\end{split}
\]
所以\ $P$ 非奇异。又有
\[
\begin{split}
B_1 P
&= B_1 M_1 B_2 \\
&= B_1 M_1 B_2 (N_2 C_2)^T \\
&= B_1 M_1 B_2 C_2^T N_2^T \\
&= B_1 M_1 B_1 C_1^T N_2^T \\
&= B_1 C_1^T N_2^T \\
&= B_2 C_2^T N_2^T \\
&= B_2 (N_2 C_2)^T = B_2
\end{split}
\]
又有
\[
\begin{split}
& B_1 C_1^T = B_2 C_2^T \\
\Longrightarrow & M_1 B_1 C_1^T = M_1 B_2 C_2^T \\
\Longrightarrow & C_1^T = P C_2^T \\
\Longrightarrow & P^{-1} C_1^T = C_2^T \\
\end{split}
\]
\end{proof}

\begin{quest}
\label{quest:154}
$\operatorname{rank}C_{r\times n}=r$,
$B \in \mathcal{R}^{r\times r}$，求证：
\begin{enumerate}
\item
$BC=0\Longrightarrow B=0$
\item
$BC=C\Longrightarrow B=I$
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:155}
$B$ 列线性无关，$BA=C$，求证：
$C$ 列线性无关的充要条件为\ $A$ 列线性无关。
\end{quest}

\begin{quest}
\label{quest:156}
$A=(\alpha_{ij})$ 为对角优势矩阵，求证：
\begin{enumerate}
\item
$\abs{A}\neq0$；
\item
当\ $\alpha_{ii}>0,i=1,2,\dotsc,n$ 时，有\ $\abs{A}>0$。
\end{enumerate}
\end{quest}

\begin{quest}
\label{quest:157}
\end{quest}

\begin{quest}
\label{quest:158}
\end{quest}

\begin{quest}
\label{quest:159}
\end{quest}

\begin{quest}
\label{quest:160}
\end{quest}

\begin{quest}
\label{quest:161}
\end{quest}

\begin{quest}
\label{quest:162}
\end{quest}

\begin{quest}
\label{quest:163}
\end{quest}

\begin{quest}
\label{quest:164}
\end{quest}

\begin{quest}
\label{quest:165}
\end{quest}

\begin{quest}
\label{quest:166}
\end{quest}


%\chapter{矩阵理论}
\backmatter

\bibliographystyle{plainnat}
\bibliography{../../bib/bib_book}

\newpage
\end{CJK*}
\end{document}

%\begin{quest}
%%\label{quest:}
%\end{quest}
%\begin{proof}
%$ $
%
%\end{proof}