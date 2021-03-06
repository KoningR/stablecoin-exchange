from pyipv8.ipv8.keyvault.crypto import default_eccrypto

if __name__ == '__main__':
    """
    Short helper method to create a new ec.pem file and store it.
    """

    filepath = ".ssh/eurotoken/trustchain/new_ec.pem"

    key = default_eccrypto.generate_key("curve25519")
    with open(filepath, "wb") as file:
        file.write(key.key_to_bin())
