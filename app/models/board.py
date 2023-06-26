from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.board_id,
            "title": self.title,
            "owner": self.owner,
        }
    
    @classmethod
    def from_dict(cls, board_data):
        new_board = cls(
            title = board_data["title"],
            owner = board_data["owner"],
        )
        
        return new_board