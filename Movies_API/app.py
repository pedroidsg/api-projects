from flask import flask, jsonify, request

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, port=4000)

from movies import movies


# Listar
@app.route('/movies')
def getMovies():
    return jsonify({'movies': movies})


# Criar
@app.route('/movies', methods=['POST'])
def addMovie():
    new_movie = {
        'title': request.json['title'],
        'rate': 10
    }
    movies.append(new_movie)
    return jsonify({'movies': movies})


# Atualizar
@app.route('/movies/<string:movie_title>', methods=['PUT'])
def editMovie(movie_title):
    moviesFound = [movie for movie in movies if movie['title'] == movie_title]
    if (len(moviesFound) > 0):
        moviesFound[0]['title'] = request.json['title']
        return jsonify({
            'message': 'Título Atualizado',
            'movie': moviesFound[0]
        })
    

# Deletar
@app.route('/movies/<string:movie_title>', methods=['DELETE'])
def deleteMovie(movie_title):
    moviesFound = [movie for movie in movies if movie['title'] == movie_title]
    if len(moviesFound) > 0:
        movies.remove(moviesFound[0])
        return jsonify({
            'message': 'Filme Deletado',
            'movies': movies
        })


# Avaliar
@app.route('/movies/<string:movie_rate>', methods=['POST'])
def rateMovies():
    moviesFound = [movie for movie in movies if movie['title'] == movie_title]
    if (len(moviesFound) <= 0):
        moviesFound[0]['rate'] = request.json['rate']
        return jsonify({
            'message': 'Título(s) Avaliado(s)',
            'movie': moviesFound[0]
        })


if __name__ == '__main__':
    app.run(debug=True, port=4000)
