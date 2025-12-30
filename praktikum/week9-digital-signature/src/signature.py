from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

print("=== GENERATE KEY RSA ===")
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

print("Private Key Length :", len(private_key.export_key()))
print("Public Key Length  :", len(public_key.export_key()))
print()

message = b"Hello, ini pesan penting."
h = SHA256.new(message)

signature = pkcs1_15.new(private_key).sign(h)

print("=== SIGNATURE ===")
print("Message :", message.decode())
print("SHA-256 :", h.hexdigest())
print("Signature (hex):")
print(signature.hex())
print()

print("=== VERIFIKASI PESAN ASLI ===")
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan VALID untuk pesan asli.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan TIDAK VALID.")
print()

fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

print("=== VERIFIKASI PESAN PALSU ===")
print("Fake Message :", fake_message.decode())
print("SHA-256 Fake :", h_fake.hexdigest())

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (INI TIDAK BOLEH TERJADI).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan TIDAK COCOK dengan pesan palsu.")
print()

print("=== SELESAI ===")