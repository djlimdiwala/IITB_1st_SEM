In this assignment, Report is made using latex. 
I have used differnt type of plots like Pie chart, Line chart, Bar chart and Histogram. these plots are generated from solution.py which is solution to the previous assignment. Tables are also made using this file. datafames are converted to latex tables using to_latex method. 

Total three tables and seven figures are generated. To generate them, run the following command--

$python3 solution.py

This will generate all files.

Tables are included in latex file using \input method. One such example is --

\begin{table}[H]
	\centering
	\input{table2}
	\label{table with column headings "Country", "Transaction", "Value"}
	\caption{table with column headings "Country", "Transaction", "Value"}
\end{table}


Figures are included using \includegraphics method with float option [H]
Tables are stored with names as table1.tex, table2.tex, table3.tex
figures are stored as image_1.jpg, image_2.jpg, image_3.jpg, image_4.jpg, image_5.jpg, image_6.jpg, image_7.jpg


To generate pdf file, run this command--

$ pdflatex --jobname=173050061_report report.tex ; pdflatex --jobname=173050061_report report.tex