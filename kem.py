#######################################################################
# KEM example. For research purposes only. Use at your own risk
#######################################################################

from pprint import pprint
import oqs
import sys

print("-----------------------------------------")
#kems = oqs.get_enabled_KEM_mechanisms()
#print("How many KEM algorithms we support?:")
#pprint(kems)

# create client and server with sample KEM mechanisms
kemalg = "Kyber1024"
''' Kyber768
    Kyber1024
    Kyber512-90s
    Kyber768-90s
    Kyber1024-90s
'''
client = oqs.KeyEncapsulation(kemalg)
#client = oqs.KeyEncapsulation(sys.argv[1])

server = oqs.KeyEncapsulation(kemalg)
public_key = client.generate_keypair()
#secret_key = client.export_secret_key()
#print(public_key.hex())

ciphertext, shared_secret_server = server.encap_secret(public_key)

#print(ciphertext.hex())
#print("\n\n")
#shared_secret_client = client.decap_secret(ciphertext)
#print(shared_secret_client.hex())
#print("\nShared secretes coincide:", shared_secret_client == shared_secret_server)


#ciphertext, shared_secret_server = server.encap_secret(public_key)
#print(ciphertext.hex())
#print(len(ciphertext))

shared_secret_client = client.decap_secret(ciphertext)
print("\nShared secretes coincide:", shared_secret_client == shared_secret_server)

# ##################################################################

with oqs.KeyEncapsulation(kemalg) as client:
    with oqs.KeyEncapsulation(kemalg) as server:

        print("\nKEM algorithm chosen:",end=' ')
        print(client.details['name'])    #print(client.alg_name)
        print("NIST level:"+str(client.details['claimed_nist_level']))
        print("IND_CCA:"+str(client.details['is_ind_cca']))
        print("\n")

        # client generates its keypair
        public_key = client.generate_keypair()

        secret_key = client.export_secret_key()

        # optionally, the secret key can be obtained by calling export_secret_key()
        # and the client can later be re-instantiated with the key pair:
        # secret_key = client.export_secret_key()
        # store key pair, wait... (session resumption):
        # client = oqs.KeyEncapsulation(kemalg, secret_key)

        print("PUBLIC KEY CREATED - CLIENT - Public key Size ["+str(client.details['length_public_key'])+"]")
        print(public_key.hex())
        #print(len(public_key))

        print("\nSECRET KEY CREATED - CLIENT - Secret key Size ["+str(client.details['length_secret_key'])+"]")
        print(secret_key.hex())
        #print(len(secret_key))

        # the server encapsulates its secret using the client's public key
        ciphertext, shared_secret_server = server.encap_secret(public_key)

        print("\nCiphertext from Server - Ciphertext Size ["+str(client.details['length_ciphertext'])+"]")
        print(ciphertext.hex())
        #print(len(ciphertext))

        print("\nShared secret size:",end=' ')
        print(client.details['length_shared_secret'])

        print("\nSHARED Secret sent from SERVER:")
        print(shared_secret_server.hex())

        # the client decapsulates the the server's ciphertext to obtain the shared secret   (Secret key client)
        shared_secret_client = client.decap_secret(ciphertext)

        print("RECOVERED SHARED Secret in CLIENT:")
        print(shared_secret_client.hex())

        print("\nShared secretes coincide:", shared_secret_client == shared_secret_server)
