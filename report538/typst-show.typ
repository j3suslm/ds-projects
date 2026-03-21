#show: content => report(
$if(title)$
  title: [$title$],
$endif$
$if(author)$
  author: [$author$],
$endif$
$if(date)$
  date: [$date$],
$endif$
$if(abstract)$
  abstract: [$abstract$],
$endif$
$if(toc)$
  toc: [$toc$],
$endif$
$if(lot)$
  lot: [$lot$],
$endif$
$if(bibfile)$
  bibfile: [$bibfile$],
$endif$
  content,
)
