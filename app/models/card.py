from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message =  db.Column(db.String, nullable=False)
    likes_count = db.Column(db.Integer, nullable=True, default=0)
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'), nullable=True)
    board = db.relationship("Board", back_populates="cards")

    def to_dict(self):

        card_dict = {
            "id": self.card_id,
            "message": self.message,
            "likes_count": self.likes_count
        }
        # if self.likes_count:
        #     card_dict["likes_count"] = self.likes_count
        # else:
        #     card_dict["likes_count"] = 0
        
        return card_dict
    
    @classmethod
    def from_dict(cls, card_data):
        new_card = cls(
            message = card_data["message"],
            likes_count = 0,
        )

        # likes_count = card_data["likes_count"]
        return new_card