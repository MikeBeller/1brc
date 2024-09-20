import polars as pl
c=pl.col
r=(pl.scan_csv('data/measurements.txt',separator=';',
               schema=pl.Schema({'sta':pl.Utf8,'val':pl.Float64}),
               has_header=False)
   .group_by('sta')
   .agg(avg=c('val').mean(), max=c('val').max(), min=c('val').min())
   .collect())
    
print(r)
