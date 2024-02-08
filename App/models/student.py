from App.database import db
from .user import User

class Student(User):
	__tablename__ = 'student'
	ID = db.Column(db.String(10), primary_key=True)
	degree = db.Column(db.String(120), nullable=False) 
    admittedTerm = db.Column(db.String(120), nullable=False)
	yearOfStudy = db.Column(db.Integer, nullable=False)
	reviews = db.relationship('Review', backref='student', lazy='joined')
	pendingReviews = db.relationship('Review', backref='pending', lazy='joined')
	karmaID = db.Column(db.Integer, db.ForeignKey('karma.karmaID'))

	def __init__(self, ID, username,firstname, lastname, email, password, faculty, admittedTerm, yearofStudy,degree):
		super().__init__(username, firstname, lastname, email, password, faculty)
		self.studentID = ID
		self.admittedTerm = admittedTerm
		self.yearOfStudy = yearofStudy
        self.degree= degree
		self.reviews = [] 
		self.pendingReviews = []
	
	def get_id(self):
		return self.ID

#Gets the student details and returns in JSON format
	def to_json(self):
		karma = self.getKarma()
		return {
        "studentID": self.studentID,
        "username": self.username,
        "firstname": self.firstname,
        "lastname": self.lastname,
		"email": self.email,
		"faculty": self.faculty,
        "degree": self.degree,
        "admittedTerm": self.admittedTerm,
        "yearOfStudy": self.yearOfStudy,
        "reviews": [review.to_json() for review in self.reviews],
		"pendingReviews": [review.to_json() for review in self.pendingReviews],
		"karmaScore": karma.score if karma else None,
        "karmaRank": karma.rank if karma else None
    }

# #Allow students to submit a review about themselves to a teacher for validation
#     def proposeReview(self);

# # Allow students to submit a recommendation request to a teacher of choice (certain points achievedS)
#     def requestRecommendation(self):


# #get karma record from the karma table using the karmaID attached to the student
# 	def getKarma(self):
# 		from .karma import Karma
# 		return Karma.query.get(self.karmaID)
