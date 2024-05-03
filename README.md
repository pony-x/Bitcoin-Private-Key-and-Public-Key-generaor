# Bitcoin Private and Public Key Generator

This Python script generates a Bitcoin private and public key pair.

## Usage

1. Make sure you have Python installed on your system.

2. Install the required dependencies by running the following command:
   ```
   pip install base58
   ```

3. Run the script by executing the following command in your terminal or command prompt:
   ```
   python generate_private_key.py
   ```

4. The script will generate a random private key and derive the corresponding public key. Both the private key and the public key will be displayed in the terminal.

## How It Works

1. **Generating a Private Key**: The script uses a cryptographically secure random number generator to generate 32 random bytes, which are then converted into a 256-bit integer to serve as the private key.

2. **Elliptic Curve Arithmetic**: Several functions are defined to perform elliptic curve arithmetic on the secp256k1 curve, which is used in Bitcoin. These functions implement mathematical operations for adding points, doubling points, scalar multiplication, and compressing points on the elliptic curve.

3. **Deriving the Public Key**: The private key is used to compute the corresponding compressed public key using elliptic curve arithmetic. Scalar multiplication of the base point \( G \) by the private key is performed to obtain the public key point.

4. **Encoding Keys**: The private key is encoded in Wallet Import Format (WIF), which involves adding prefix and suffix bytes and calculating a checksum. The public key is encoded using Base58Check encoding, adding a prefix byte and calculating a checksum.

5. **Printing Keys**: Finally, both the private key (in WIF format) and the public key (in Base58Check encoding) are printed to the terminal.

## Dependencies

- base58


