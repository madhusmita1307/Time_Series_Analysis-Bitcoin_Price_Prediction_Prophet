# Time Series Analysis For Bitcoin Price Prediction Using Prophet 📈

Project Demo Video Link : [Click Here](add link)<br>
Project Report:  [Click Here](add link)

This repository hosts a collection of code and data for performing Time Series Analysis on Bitcoin price data. The pre-trained Prophet model leverages historical price and market data to forecast future trends and fluctuations in the Bitcoin market. The code provides comprehensive tools for data preprocessing, feature engineering, model training, and evaluation. It serves as a valuable resource for researchers, enthusiasts, and developers interested in Bitcoin price prediction using time series analysis techniques.

## Model Details 🔎

The bitcoin price prediction model is built using Python and the Flask web framework. With the help of Facebook's Prophet Library, we have constructed a predictive model and this will help us to analyze historical price data and consider factors like trends, seasonality, and holidays to provide useful information for investors, traders, and researchers in the cryptocurrency marke. The model takes into account various features such as date, open price, low, high, close, adj close, and volume.

The trained model is serialized using the pickle library and stored in the `crypto.pkl` file.

## Usage :rocket:

To use the bitcoin price prediction model, follow the steps below:

1. Clone the repository:  :open_file_folder::
```
git clone https://github.com/your-username/Time_Series_Analysis-Bitcoin_Price_Prediction_Prophet.git
```
2. Install the required dependencies: :package::
```
pip install -r requirements.txt
```
4. Run the Flask web application: :computer::

5. Open your web browser and visit `http://localhost:5000` to access the prediction interface.

6. Select the date for which you want to view the forecasted price of Bitcoin in the provided form and submit it.

7. The model will process the input and display the predicted price on that particular date.

Feel free to modify the `app.py` file and the HTML templates in the `templates` directory to customize the user interface or incorporate additional functionality.

## Repository Structure :file_folder:

The repository is structured as follows:
```
BITCOIN-Prediction/
├── app.py
├── crypto.pkl
├── Time_Series_Analysis_for_Bitcoin_Price_Prediction.ipynb
├── templates/
│  ├── index.html
│  ├── about.html
│  ├── predict.html
├── static/
│  ├── css
│  │  ├── main.css
└── README.md
```

- `app.py`: Contains the Flask application code, including the routes for handling user requests and making predictions using the trained model.
- `crypto.pkl`: Serialized machine learning model saved as a pickle file.
- `Time_Series_Analysis_for_Bitcoin_Price_Prediction.ipynb`: Contains the python code for Bitcoin Prediction Model.
- `templates/`: Directory containing HTML templates for the web interface.
- `static/`: Directory contains the CSS file and images used.
- `README.md`: This readme file providing information about the project.

## Contributing :handshake:

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.
