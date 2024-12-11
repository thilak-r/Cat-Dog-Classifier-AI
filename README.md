# Cat and Dog Classifier 🐾

This project is an **Animal Classifier** that uses machine learning to classify images of animals. The model is trained using a deep learning approach and is deployed on a web platform for easy accessibility.

## Features

- Classify animal images into different categories.
- Pre-trained model file: `animal_classifier_model.h5` (stored using Git LFS).
- Web interface for easy image uploads and classification.
- RESTful API available for external integrations.
- Deployment-ready with support for cloud platforms like Vercel.


## Installation

To run the project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/thilak-r.git
    cd thilak-r
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure the `animal_classifier_model.h5` is downloaded using Git LFS:

    ```bash
    git lfs pull
    ```

4. Start the application:

    ```bash
    ./start.sh
    ```

    Alternatively, you can manually start the application using Python:

    ```bash
    python cv.py
    ```

## Usage

Once the server is running, you can access the web interface by navigating to `http://localhost:5000` in your browser.

1. Upload an image of an animal.
2. Click on the "Classify" button to see the prediction results.
3. The classification result will show the predicted animal category.

## Deployment

The project can be deployed on platforms like **Vercel** or **Heroku**. Use the provided `Procfile` for deployment on Heroku, and the `vercel.json` for Vercel configuration.

### Deploying on Vercel

1. Install the Vercel CLI:

    ```bash
    npm install -g vercel
    ```

2. Run the following command to deploy:

    ```bash
    vercel
    ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

<br><br>
under guidance of [Dr Agughasi Victor Ikechukwu](https://github.com/Victor-Ikechukwu)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
