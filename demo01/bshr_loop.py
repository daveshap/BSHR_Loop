import openai
import requests
import json



def bshr_loop(query):
    all_search_results = list()  # this should be a list of dicts with something like "query", "source", and "content" 
    all_hypotheses = list()  # this should be a list of strings
    while True:
        ## STEP 1: BRAINSTORM
        search_queries = generate_search_queries(query, all_search_results, all_hypotheses)  # will generate new search queries based upon main query, all results, and all hypotheses)
        # TODO write generate_search_queries function
        
        ## STEP 2: SEARCH
        new_search_results = execute_searches(search_queries)  # will retrieve more information from assigned data source
        # TODO write execute_searches function
        # TODO update all_search_results object with new results
        
        ## STEP 3: HYPOTHESIZE
        new_hypothesis = generate_new_hypothesis(query, all_search_results, all_hypotheses)  # will generate new and improved hypothesis based on all available data
        # TODO write generate_new_hypothesis function
        # TODO update all_hypotheses object
        
        ## STEP 4: REFINE
        satisficed = check_satisficed(query, all_search_results, all_hypotheses)  # test if the main query has been satisficed 
        # TODO write check_satisficed function
        if satisficed:
            return all_search_results, all_hypotheses
        
        exhausted = check_exhausted(query, all_search_results)  # test if we seem to have exhausted all available information
        # TODO write check_exhausted function
        if exhausted:
            return all_search_results, all_hypotheses
        
        ## if neither test is satisfied, the loop will recurse, repeating the cycle of brainstorming, searching, and hypothesizing, thus further refining the answer.
    



if __name__ == '__main__':
    # this is the primary loop
    while True:
        # Get user query
        main_query = input('\n\n\n#########\n\n\nWhat is your query? ')
        if main_query.lower() == 'exit'
            exit(0)
        
        # start BSHR loop
        evidence, hypothesis = bshr_loop(main_query)
        
        # render answer
        answer = synthesize_main_answer(evidence, hypotheses)  # TODO write this function
        print('\n\n\nANSWER:\n\n\n', answer)