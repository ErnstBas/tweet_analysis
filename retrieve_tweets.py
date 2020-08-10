import twint

# Configure
c = twint.Config()
c.Search = "spacex"
c.Lang = "english"
c.Since = "2020-08-01"
c.Until = "2020-08-03"
c.Store_csv = True 
c.Output = "spacex.csv"

# Run
twint.run.Search(c)
