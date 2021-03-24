from flask import render_template, request
from CTFd.plugins.challenges import BaseChallenge, CHALLENGE_CLASSES


#création de la classe de challenge php
class PhpChallengeType(BaseChallenges):
    __mapper__args__ = {'polymorphic_identity' : 'php'}
    #mettre la base de donnée à jour si necessaire ici

    def __init__(self, name, description, value, category, type='php') :
        self.name = name
        self.description = description
        self.value = value
        self.category = category
        self.type = type


    #Exemple de code pour la commande create
    @staticmethod
	def create(request):
		"""
		This method is used to process the challenge creation request.

		:param request:
		:return:
		"""

        UPLOAD_FOLDER = '~/chall_to_add'
        ALLOWED_EXTENSIONS = {'zip'}

        if request.method == 'POST' :
            f = request.files['file']
            f.save(secure_filename(f.filename))
    		data = request.form or request.get_json()

		return challenge

def load(app) :
    #app.db.create_all()
    CHALLENGE_CLASSES['php'] = PhpChallengeType
    register_plugin_assets_directory(app, base_path='/plugins/Php_Challenge/assets/')
