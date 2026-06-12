from flask import Flask, request, jsonify

app = Flask(__name__)

def caesar_encrypt(plain_text, key):
    encrypted = ""
    for char in plain_text:
        if char.isalpha():
            shift = int(key) % 26
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(cipher_text, key):
    decrypted = ""
    for char in cipher_text:
        if char.isalpha():
            shift = int(key) % 26
            if char.isupper():
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += char
    return decrypted

@app.route('/api/caesar/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_message = caesar_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_message})

@app.route('/api/caesar/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_message = caesar_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)