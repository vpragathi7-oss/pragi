from flask import Flask, render_template, request

app = Flask(__name__)

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

@app.route("/", methods=["GET", "POST"])
def home():
    encrypted = ""
    decrypted = ""

    if request.method == "POST":
        message = request.form["message"]
        shift = int(request.form["shift"])

        encrypted = encrypt(message, shift)
        decrypted = decrypt(encrypted, shift)

    return render_template("index.html",
                           encrypted=encrypted,
                           decrypted=decrypted)

if __name__ == "__main__":
    app.run(debug=True)