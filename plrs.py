import polars as pl
r=(pl.scan_csv('data/measurements.txt',separator=';',
               schema=pl.Schema({'sta':pl.Utf8,'val':pl.Float64}),
               has_header=False)
   .group_by('sta')
   .agg(pl.col('val').mean().alias('avg'),
        pl.col('val').max().alias('max'),
        pl.col('val').min().alias('min'))
   .collect())
    
print(r)
