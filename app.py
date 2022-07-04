#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request
import joblib


# In[2]:


lr_model = joblib.load("RegressionPrediction")
dt_model = joblib.load("DecisionTreePrediction")


# In[3]:


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            rates = float(request.form.get("rates"))
        except ValueError:
            return render_template("index.html", result1 = "Waiting",result2 = "Waiting")
        else:
            lr_result = lr_model.predict([[rates]]);
            dt_result = dt_model.predict([[rates]]);
            return render_template("index.html", result1 = lr_result,result2 = dt_result)
    else:
        return render_template("index.html", result1 = "Waiting",result2 = "Waiting")


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




