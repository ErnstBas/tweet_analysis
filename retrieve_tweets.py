import twint

# Configure
c = twint.Config()
c.Search = "Your Search Term"
c.Lang = "english"
c.Since = "startdate yyyy-mm-dd"
c.Until = "enddate yyyy-mm-dd"
c.Store_csv = True 
c.Output = "Filename.csv"

# Run
twint.run.Search(c)
