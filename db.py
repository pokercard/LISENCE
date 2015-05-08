class _Engine(object):
	def __init__(self,connect):
		self._connect = connect
	def connect(self):
		return self._connect()

engine = None

class _Dbctx(threading.local):
	def __init__(self):
		self.connection = None
		self.transaction = 0

	def is_init(self):
		return not self.connection is None

	def init(self):
		self.connection = _LasyConnection()
		self.transaction = 0

	def cleanup(self):
		self.connection.cleanup()
		self.connection = None

	def cursur(self):
		return self.connection.cursor()

_db_ctx=_Dbctx()




