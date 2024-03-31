class Aggregate:
    def __init__(self) -> None:    
        self.reaction_counter = {}

    def increment_counters(self,poem):
            reactions = self.reaction_counter[poem['id']]  
            if poem['reaction'] == 'Like': 
                reactions['likes']+=1
            elif poem['reaction'] == 'Love':
                reactions['loves']+=1
            elif poem['reaction'] == 'insightful':
                reactions['insightful']+=1
            elif poem['reaction'] == 'clap':
                reactions['clap']+=1
            self.reaction_counter[poem['id']] = reactions      

    def modified_data(self,poems):
            final_data = []
            for poem in poems:
                reactions = self.reaction_counter[poem['id']]
                temp = {
                     'id' : poem.get('id'),
                     'posted_by' : poem.get('posted_by'),
                     'reacted_by_user' : poem.get('reacted_by_user',None),
                     'name' : poem.get('name'),
                     'author' : poem.get('author',''),
                     'interpretation' : poem.get('interpretation',''),
                     'likes' : reactions.get('likes',0),
                     'loves' : reactions.get('loves',0),
                     'insightful' : reactions.get('insightful',0),
                     'clap' : reactions.get('clap',0)
                }
                if temp not in final_data:
                    final_data.append(temp)

            return final_data

                
         

    def aggregate_reactions(self,poems):
        for poem in poems:
                if poem['id'] not in self.reaction_counter.keys():
                        self.reaction_counter[poem['id']] = {
                            'likes' : 0,
                            'loves' : 0,
                            'insightful' : 0,
                            'clap' : 0
                        }
                self.increment_counters(poem)

        return self.modified_data(poems)
            




