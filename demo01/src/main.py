from system01_brainstorm import brainstorm
from system02_hypothesize import hypothesize
from system03_satisfice import satisfice
from system04_refine import refine

def main():
    user_query = input("Enter a naive query :) -> ")
    total_tokens = 0
    notes = ""
    queries = ""
    iteration = 0
    max_iterations = 3
    hypotheses_feedback = "# FEEDBACK ON HYPOTHESES\n"

    while True:
        iteration += 1
        print(f"{iteration=} started")

        new_queries, notes, tokens = brainstorm(
            user_query=user_query,
            notes=notes, 
            queries=queries,
        )
        queries += new_queries

        total_tokens = track_token_usage(total_tokens, tokens)

        new_hypothesis, tokens = hypothesize(
            user_query=user_query,
            notes=notes,
            hypotheses=hypotheses_feedback,
        )

        total_tokens = track_token_usage(total_tokens, tokens)

        satisficed, feedback, tokens = satisfice(
            user_query=user_query,
            notes=notes,
            queries=queries,
            hypothesis=new_hypothesis,
        )

        total_tokens = track_token_usage(total_tokens, tokens)

        hypotheses_feedback = (
f"""
{hypotheses_feedback}

## HYPOTHESIS
{new_hypothesis}

## FEEDBACK
{feedback}
"""
        )
        print(f"{new_hypothesis=}")
        print(f"{satisficed=}")
        print(f"{feedback=}")

        if satisficed or max_iterations <= iteration:
            print(f"reached max iterations {max_iterations <= iteration}")
            break
        
        notes, tokens = refine(notes)

        total_tokens = track_token_usage(total_tokens, tokens)
        print(f"{iteration=} completed")

def track_token_usage(total_tokens, tokens):
    print(f"{tokens=}")
    total_tokens += tokens
    print(f"{total_tokens=}")
    return total_tokens

if __name__ == "__main__":

    main()


# what is at the bottom of the deepest part of the deepest ocean?