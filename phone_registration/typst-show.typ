#show: body => report(
  title: [$title$],
  $if(subtitle)$ 
    subtitle: [$subtitle$],
  $endif$
  $if(abstract)$ 
    abstract: [$abstract$],
  $endif$
  $if(author)$ 
    author: "$author$",
  $endif$
  date: [$date$],
  toc: $if(toc)$$toc$$else$false$endif$,
  lof: $if(lof)$$lof$$else$false$endif$,
  lot: $if(lot)$$lot$$else$false$endif$,
  body
)
