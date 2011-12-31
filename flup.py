
from token_grid import TokenGrid
import tokens
import random
import copy

class Game( object ):
    def __init__( self, width, height, gametype, ntokens):
        self.grid = TokenGrid( width, height )
        self.tokens = tokens.selectRandomNTokens( ntokens )  
        self.laziness = 30
        self.numberOfInitialTokens = 100

        # Initialize Board
        if gametype == "Clear":
            pass
        elif gametype == "Solution":
            self.completelySolve()
        else: #default gametype
            self.ten_turns_in()

        self.selectValidToken()
    
    def ten_turns_in( self ):
        for i in range( 0, 10 ):
            self.autoplayOneTurn()

    def selectValidToken( self ):
        result = self.solveOneStep()
        if not result: 
            self.gameOver = True
            return 
        token, point = result
        self.currentToken = token
    
    def completelySolve( self ):
        while( self.solveOneStep( ) ):
            pass
    
    def solveForToken( self, token ):
        """ Returns all valid placements for the token. """ 
        valid_placements = [] 
        for point in self.grid.points():
            if test_token.isValid( self.grid, point) and not self.grid.isAnyTokenAtPoint( point ):
                valid_placements.append( point )
            if len( valid_placements ) > self.laziness:
                break
        return valid_placements

    def solveOneStep( self, temp_tokens = [] ):
        if temp_tokens == []:
            temp_tokens = copy.deepcopy( self.tokens ) 
        test_token = random.choice( temp_tokens )
        
        valid_placements = self.solveForToken( test_token ) 
        if len(valid_placements) == 0 and len(temp_tokens) <= 1:
            return False
        if len(valid_placements) == 0:
            temp_tokens.remove( test_token )
            return self.solveOneStep( temp_tokens )

        place_point = random.choice(valid_placements)
        return ( test_token, place_point ) 

    def autoplayOneTurn( self ): 
        token, point = self.solveOneStep( self )
        if self.grid.placeToken( token, point ):
            return True
        else:
            print "Somehow our valid placement is not valid - ", point
            print self.grid.error
            return self.autoplayOneTurn( )
        

if __name__ == '__main__':
    g = Game( 10, 10, "Solution", 10)
    print g.grid