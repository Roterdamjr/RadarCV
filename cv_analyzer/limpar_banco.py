from database import AnalyzeDatabase

database = AnalyzeDatabase()
database.jobs.truncate()  # Limpa todos os registros da tabela "jobs"
database.files.truncate()