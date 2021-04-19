class Program:
  def __init__(self, name, year):
      self._name = name.title()
      self.year = year
      self._likes = 0

  @property
  def likes(self):
      return self._likes

  def set_like(self):
      self._likes += 1

  @property
  def name(self):
      return self._name

  @name.setter
  def name(self, name):
      self._name = name

  def __str__(self):
      return f'Nome: {self.name} Likes: {self.likes}'


class Movie(Program):
  def __init__(self, name, year, duration):
    super().__init__(name, year)
    self.duration = duration

  def __str__(self):
      return f'Nome: {self.name} - {self.duration} min - Likes: {self.likes}'


class Serie(Program):
  def __init__(self, name, year, seasons):
    super().__init__(name, year)
    self.seasons = seasons
    
  def __str__(self):
      return f'Nome: {self.name} - {self.seasons} temporadas - Likes: {self.likes}'


class Playlist:
  def __init__(self, name, programs):
    self.name = name
    self._programs = programs

  def __getitem__(self, item):
    return self._programs[item]

  def __len__(self):
    return len(self._programs)

  @property
  def list_programs(self):
    return self._programs

  @property
  def size_programs(self):
    return len(self._programs)


vingadores = Movie('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Movie('Todo mundo em pânico', 199, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.set_like()
tmep.set_like()
tmep.set_like()
tmep.set_like()
tmep.set_like()
demolidor.set_like()
demolidor.set_like()
atlanta.set_like()
atlanta.set_like()
atlanta.set_like()

movies_and_series = [vingadores, atlanta, demolidor, tmep]
playlist_weekend = Playlist('fim de semana', movies_and_series)

print('Tamanho da playlist: {}'.format(len(playlist_weekend)))

for program in playlist_weekend:
  print(program)