from flask import Flask, render_template, request, flash


from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError
c = CurrencyRates()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fenway2023'


@app.route('/')
def home_page():
    
       
        rates=c.get_rates("USD")
        availExchanges = list(rates)
        return render_template('home.html', exchanges=availExchanges)
   
       
   
    

@app.route('/calc', methods=['POST'])
def calc():
    codes = CurrencyCodes()
    
    #gets currency from
    begCurr = request.form.get("begCurr").upper()

    #gets currency to
    endCurr = request.form.get("endCurr").upper()
    #gets amount to convert
    amt = request.form.get("amt")
    
    #gets available currencys for echnage
    rates=c.get_rates("USD")
    #for currency validation
    
    availExchanges = list(rates)
    
    
    #checks to make sure we have a valid float for conversion
    flAmt = checkFloat(amt)
    if not flAmt:
         #checks to see if our currencys are valid even though we know at this point the amount is invalid
         curOk = checkCur(begCurr, endCurr)
         return render_template('home.html', exchanges=availExchanges )


    #this function validates currencys
    curOk = checkCur(begCurr, endCurr)
   

    if curOk:
        #converted does the calculation with the API
       
        amt = float(amt)
    
        converted =convert(begCurr, endCurr, amt)
    else:
         return render_template('home.html', exchanges=availExchanges )
         
         
     
    roundedConvert =round(converted, 2)
    endSymbol = codes.get_symbol(endCurr)
    begSymbol = codes.get_symbol(begCurr)
    return render_template('calc.html', beg = begSymbol, begAmt=amt, end=endSymbol, endAmt=str(roundedConvert), bcurr=begCurr, ecurr=endCurr )
    


def checkFloat(amt):
    try:
        flAmt = float(amt)
        return True
    except:
         
         flash('please enter only currency in 123.45 form!')
         
         return False
    #validates the currency types
def checkCur(begCurr, endCurr):
    try:
        converted =c.convert(begCurr, endCurr, 10)
        return True
    
    #this reads the error returned from the API and defines them for the user
    except RatesNotAvailableError as e:
         #this error means the conversion TO currency does not exist in database
         if "Currency https://theforexapi.com/api/latest" in str(e):
            flash(f'{endCurr} is not a valid Currency!')
            return False
         #I set this up in case in the future we want to change the FROM currency from the drop box to input.  This would catch if the user inputed
         # a bad currency in a future version, but since we are using a drop box now the user can't input a bad input.
         if "Currency Rates Source Not Ready" in str(e):
              print('conversion from wrong')
              return False
         
#does the acutal conversion
def convert(begCurr, endCurr, amt):
     num =c.convert(begCurr, endCurr, amt)
     return num
