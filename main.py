import streamlit as st
from crypto_utils import xor_cipher, rc4_cipher, des_cipher, aes_cipher
from utils import base64_handler

st.title("Aplikasi Kriptografi Sederhana")

# Pilih algoritma
algo = st.selectbox("Pilih Algoritma:", ["Simple XOR", "RC4", "DES", "AES"])
mode = None

if algo in ["DES", "AES"]:
    mode = st.selectbox("Pilih Mode:", ["ECB", "CBC", "Counter"])

# Input pesan atau file
input_type = st.radio("Pilih Input:", ["Teks", "File"])
key = st.text_input("Masukkan Kunci:")

# Jika input berupa file, tampilkan opsi untuk menentukan nama file output
if input_type == "File":
    output_filename = st.text_input("Nama File Output (beserta ekstensi, contoh: hasil.txt):", "hasil.txt")

ciphertext = None  # Menyimpan hasil enkripsi
decrypted_data = None  # Menyimpan hasil dekripsi

if input_type == "Teks":
    plaintext = st.text_area("Masukkan Teks:")

    if st.button("Enkripsi"):
        if not plaintext:
            st.error("Masukkan teks terlebih dahulu!")
        else:
            if algo == "Simple XOR":
                ciphertext = xor_cipher.encrypt(plaintext, key)
            elif algo == "RC4":
                ciphertext = rc4_cipher.encrypt(plaintext, key)
            elif algo == "DES":
                ciphertext = des_cipher.encrypt(plaintext, key, mode)
            elif algo == "AES":
                ciphertext = aes_cipher.encrypt(plaintext, key, mode)
            
            base64_output = base64_handler.to_base64(ciphertext)
            st.text_area("Hasil Enkripsi (Base64):", base64_output)

    if st.button("Dekripsi"):
        try:
            ciphertext = base64_handler.from_base64(plaintext)
            if algo == "Simple XOR":
                decrypted_data = xor_cipher.decrypt(ciphertext, key)
            elif algo == "RC4":
                decrypted_data = rc4_cipher.decrypt(ciphertext, key)
            elif algo == "DES":
                decrypted_data = des_cipher.decrypt(ciphertext, key, mode)
            elif algo == "AES":
                decrypted_data = aes_cipher.decrypt(ciphertext, key, mode)

            st.text_area("Hasil Dekripsi:", decrypted_data)
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

elif input_type == "File":
    uploaded_file = st.file_uploader("Unggah File", type=["txt", "bin", "pdf", "png", "jpg", "docx"])

    if uploaded_file is not None:
        file_bytes = uploaded_file.read()

        if st.button("Enkripsi"):
            if algo == "Simple XOR":
                ciphertext = xor_cipher.encrypt(file_bytes, key)
            elif algo == "RC4":
                ciphertext = rc4_cipher.encrypt(file_bytes, key)
            elif algo == "DES":
                ciphertext = des_cipher.encrypt(file_bytes, key, mode)
            elif algo == "AES":
                ciphertext = aes_cipher.encrypt(file_bytes, key, mode)

            # Pastikan file disimpan dalam format biner
            st.download_button("Download Hasil Enkripsi", ciphertext, file_name=output_filename)

        if st.button("Dekripsi"):
            try:
                if algo == "Simple XOR":
                    decrypted_data = xor_cipher.decrypt(file_bytes, key)
                elif algo == "RC4":
                    decrypted_data = rc4_cipher.decrypt(file_bytes, key)
                elif algo == "DES":
                    decrypted_data = des_cipher.decrypt(file_bytes, key, mode)
                elif algo == "AES":
                    decrypted_data = aes_cipher.decrypt(file_bytes, key, mode)

                # Simpan hasil dekripsi dalam format biner
                st.download_button("Download Hasil Dekripsi", decrypted_data, file_name=output_filename)
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
