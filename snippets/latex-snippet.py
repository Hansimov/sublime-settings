tex_key_list = [
    # name, trigger, content
    ['begin-itemize',       'it',    '\\begin{itemize}\n    \\item $0\n\\end{itemize}'],
    ['begin-enumerate',     'en',    '\\begin{enumerate}\n    \\item $0\n\\end{enumerate}'],
    ['item',                'i',      '\\item $0'],
    ['begin-frame',         'fr',    '\\begin{frame}\n$0\n\\end{frame}'],
    ['frametitle',          'ft',     '\\frametitle{$0}'],
    ['begin-end',           'be',     '\\begin{$0}\n\n\\end{$0}'],
    ['begin',               'b' ,     '\\begin{$0}'],
    ['end',                 'e' ,     '\\end{$0}'],
    ['begin-document',      'doc',     '\\begin{document}\n\n$0\n\n\\end{document}'],
    ['usepackage',          'up',     '\\usepackage{$0}'],

    ['documentclass',       'dc' ,    '\\documentclass{$0}'],
    ['include',             'inc' ,   '\\include{$0}'],
    ['input',               'inp' ,   '\\input{$0}'],
    ['section',             'sec',    '\\section{$0}'],
    ['subsection',          'ssec',   '\\subsection{$0}'],
    ['subsubsection',       'sssec',  '\\subsubsection{$0}'],
    ['label',               'lab',    '\\label{$0}'],
    ['caption',             'cap',    '\\caption{$0}'],
    ['ref',                 'ref',    '\\ref{$0}'],
    ['cite',                'cite',   '\\cite{$0}'],
    ['footnote',            'fn',     '\\footnote{$0}'],
    ['parencite',           'pcite',  '\\parencite{$0}'],
    ['vspace',              'vs',     '\\vspace{$0}'],
    ['vspace-baselineskip', 'vsb',    '\\vspace{0.5\\baselineskip}'],
    ['chapter',             'chap',   '\\chapter{$0}'],
    ['text-bold',           'tb',     '\\textbf{$0}'],
    ['text-italic',         'ti',     '\\textit{$0}'],
    ['begin-figure',        'fg',     '\\begin{figure}[htbp]\n$0\n\\end{figure}'],
    ['centering',           'cen',    '\\centering'],
    ['newpage',             'np',     '\\newpage'],

    ['usetikzlibrary',      'ut',     '\\usetikzlibrary{$0}'],
    ['begin-tikzpicture',   'tp',     '\\begin{tikzpicture}\n\n$0\n\n\\end{tikzpicture}'],
    ['doc-tikz',            'tdoc',   '\\documentclass[border=10pt]{standalone}\n\n\\usepackage{tikz}\n\n\\begin{document}\n\n$0\n\n\\end{document}'],
    ['tikz-draw',           'dr',     '\\draw'],
    ['tikz-node',           'n',      '\\node'],
    ['tikz-node',           'nd',     'node'],
    ['tikz-child',          'c',     'child'],
    ['tikz-tikz',           'tk',     '\\tikz']

]

for item in tex_key_list:
    name = item[0]
    trigger = item[1]
    content = item[2]
    with open('C:/Users/yuzeh/AppData/Roaming/Sublime Text 3/Packages/snippets/latex/' + name + '.sublime-snippet','w') as spfile:
        spfile.write('<snippet>\n')
        spfile.write('<content><![CDATA[' + content + ']]></content>\n') # Only difference
        spfile.write('<tabTrigger>' + trigger + '</tabTrigger>\n')
        spfile.write('<scope>text.tex</scope>\n')
        spfile.write('<description>tex: ' + name + '</description>\n')
        spfile.write('</snippet>')