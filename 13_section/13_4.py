class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"
    
    def public_method(self):
        # client が使っても良い
        pass  #passは文が必須な構文で何もしていないときに使う。

    def _unsafe_method(self):
        # client は使うべきじゃない
        pass


#_ではじまってる場合は使うべきじゃないという意味を持つ。