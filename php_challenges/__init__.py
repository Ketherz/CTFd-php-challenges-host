import os, shutil
from flask import Flask, render_template, Blueprint, flash, redirect, url_for
from CTFd.plugins.challenges import BaseChallenge, CHALLENGE_CLASSES
from CTFd.plugins import register_plugin_assets_directory
from CTFd.api.v1.challenges import Challenge
from CTFd.models import Challenges, db
from werkzeug.utils import secure_filename

import base64
import requests
import zipfile

#création de la classe de challenge php
class PhpChallengeType(BaseChallenge):
    id = "php"
    name = "php"
    templates = {
        'create': '/plugins/php_challenges/assets/create.html',
        'update': '/plugins/php_challenges/assets/update.html',
        'view': '/plugins/php_challenges/assets/view.html',
    }
    scripts = {
        'create': '/plugins/php_challenges/assets/create.js',
        'update': '/plugins/php_challenges/assets/update.js',
        'view': '/plugins/php_challenges/assets/view.js',
    }
    route = '/plugins/php_challenges/assets'
    blueprint = Blueprint('php_challenges', __name__, template_folder='templates', static_folder='assets')



    #Create is used to create the challenge (bd add and php file add)
    @staticmethod
    def create(request):
        """
        This method is used to process the challenge creation request.

        :param request:
        :return:
        """

        data = request.form or request.get_json()
        challenge = PhpChallenge(**data)
        db.session.add(challenge)
        db.session.commit()

        # Conversion du fichier et sauvegarde de celui-ci
        # TODO: Probléme de sécurité au niveau de l'upload de fichier zip, à vérifier

        with open("CTFd/plugins/php_challenges/challenges_to_add/" + str(challenge.id) + ".zip", "wb") as fh:
            fh.write(base64.decodebytes(challenge.zip_file.split("base64",1)[1].encode()))

        with zipfile.ZipFile("CTFd/plugins/php_challenges/challenges_to_add/" + str(challenge.id) + ".zip", "r") as zip_ref :
            zip_ref.extractall("CTFd/plugins/php_challenges/challenges_to_add/")
            os.remove("CTFd/plugins/php_challenges/challenges_to_add/" + str(challenge.id) + ".zip")

        return challenge




class PhpChallenge(Challenges):
    __mapper_args__ = {'polymorphic_identity': 'php'}
    zip_file = ""




def load(app) :
    #app.db.create_all()
    CHALLENGE_CLASSES['php'] = PhpChallengeType
    register_plugin_assets_directory(app, base_path='/plugins/php_challenges/assets/')
