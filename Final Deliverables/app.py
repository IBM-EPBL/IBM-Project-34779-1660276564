{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ee5e2295",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from flask import Flask,render_template,request\n",
    "import pickle\n",
    "app= Flask(__name__)\n",
    "model=pickle.load(open(r'C:\\Users\\karthick\\wqi.pkl','rb'))\n",
    "@app.route('/')\n",
    "def home() :\n",
    "  return render_template(\"front page.html\")\n",
    "@app.route('/login',methods = ['POST'])\n",
    "def login() :\n",
    "  year = request.form[\"year\"]\n",
    "  do = request.form[\"do\"]\n",
    "  ph = request.form[\"ph\"]\n",
    "  co = request.form[\"co\"]\n",
    "  bod = request.form[\"bod\"]\n",
    "  tc = request.form[\"tc\"]\n",
    "  na = request.form[\"na\"]\n",
    "  total = [[float(do),float(ph),float(co),float(bod),float(na),float(tc)]]\n",
    "  y_pred = model.predict(total)\n",
    "  y_pred = y_pred[[0]]\n",
    "  if(y_pred >= 95 and y_pred<=100):\n",
    "    return render_template(\"front page.html\",showcase = 'Excellent, The Predicted Value Is'+ str(y_pred))\n",
    "  elif(y_pred >= 89 and y_pred<=94):\n",
    "    return render_template(\"front page.html\",showcase = 'Very Good, The Predicted Value Is'+ str(y_pred))\n",
    "  elif(y_pred >= 80 and y_pred<=88):\n",
    "    return render_template(\"front page.html\",showcase = 'Good, The Predicted Value Is'+ str(y_pred))\n",
    "  elif(y_pred >= 65 and y_pred<=79):\n",
    "    return render_template(\"front page.html\",showcase = 'Fair, The Predicted Value Is'+ str(y_pred))\n",
    "  elif(y_pred >= 45 and y_pred<=64):\n",
    "    return render_template(\"front page.html\",showcase = 'Marginal, The Predicted Value Is'+ str(y_pred))\n",
    "  else:\n",
    "    return render_template(\"front page.html\",showcase = 'Poor, The Predicted Value Is'+ str(y_pred))\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "     app.run(debug = True,port=5000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4573c592",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
