from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        # retrieve data from the form
        data = {
            'Employee ID': request.form.get('employee_id'),
            'Date of Joining': request.form.get('date_of_joining'),
            'Gender': request.form.get('gender'),
            'Company Type': request.form.get('company_type'),
            'WFH Setup Available': request.form.get('wfh_setup_available'),
            'Designation': request.form.get('designation'),
            'Resource Allocation': request.form.get('resource_allocation'),
            'Mental Fatigue Score': request.form.get('mental_fatigue_score'),
            'Burn Rate': request.form.get('burn_rate')
        }
        
        # transform the data into a pandas DataFrame
        df = pd.DataFrame([data])
        
        # save the DataFrame to a csv file
        df.to_csv('survey_data.csv', mode='a', index=False)
        
        return 'Thank you for your participation!'
    else:
        return render_template('survey.html')

if __name__ == "__main__":
    app.run(debug=True)
