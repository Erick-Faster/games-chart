from game_automator.pipeline.game_extractor import GameExtractor
from game_automator.pipeline.game_transformer import GameTransformer

class GamePipeline(object):
    def __init__(self):
        self.game_extractor = GameExtractor()
        self.game_transformer = GameTransformer()

    def run(self):
        df = self.game_extractor.extract_data()
        df = self.game_transformer.transform_data(df)
        return df