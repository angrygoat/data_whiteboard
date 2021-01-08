#!/usr/bin/env python3
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import connexion
import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Data Whiteboard API'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
