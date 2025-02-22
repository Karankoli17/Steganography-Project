# Secure Data Hiding in Image Using Steganography

## 📌 Description
This Python project allows users to **hide (encode) secret messages inside images** and **retrieve (decode) them** later using **Least Significant Bit (LSB) steganography**. It is a simple command-line tool that ensures message security by embedding text inside image pixels.

## 🔥 Features
✅ **Hides text inside images** without changing their appearance.  
✅ **Extracts hidden text** from modified images.  
✅ **Prevents errors** by ensuring pixel values stay in the 0-255 range.  
✅ **Simple user interface**: Just run the script and follow the prompts.  

## ⚙️ Installation
Ensure you have Python installed, then install the required libraries:
```sh
pip install pillow numpy
```

## 🚀 Usage
Run the script and choose whether to encode or decode a message:
```sh
python steganohide.py
```

### 🎭 Encoding (Hiding a Message)
1. Enter the path of the image.
2. Enter the secret message.
3. Enter the output image filename.

### 🔍 Decoding (Extracting a Message)
1. Enter the path of the modified image.
2. The hidden message will be displayed.

## 📝 Example Usage
#### Encoding a message:
```sh
Enter the path of the image: input.png
Enter the secret message: This is a secret!
Enter the output image path: output.png
Message encoded and saved to output.png
```

#### Decoding a message:
```sh
Enter the path of the image to decode: output.png
Decoded Message: This is a secret!
```

## 📜 License
This project is open-source. Feel free to modify and improve it! 🚀

---
### 🌟 Connect with Me
🔗 [GitHub](https://github.com/Karankoli17)  
🔗 [LinkedIn](https://www.linkedin.com/in/karan-koli-4b7b5b2b2/)
