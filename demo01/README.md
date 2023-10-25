# Demo01: Basic BSHR_Loop Implementation with Wikipedia

Welcome to Demo01, a basic implementation of the BSHR_Loop using Wikipedia as a data source. This demo is designed to help you get familiar with the BSHR_Loop and its potential applications. The code for this demo is written in Python.

## Overview

In this demo, we will use Large Language Models (LLMs) to perform the Brainstorm, Search, Hypothesize, Refine (BSHR) loop. The LLM will accept user queries, brainstorm search queries, search Wikipedia for relevant information, formulate hypotheses, and refine these hypotheses based on the information gathered.

## System Messages

I have already written the following SYSTEM messages but more needs to be done. 

1. **Brainstorm Instruction**: This instruction will guide the LLM to brainstorm search queries. The LLM can generate both naive and informed queries, depending on the information provided by the user. The output of this instruction is a JSON object containing the brainstormed queries. This file is `system01_brainstorm_search_queries.txt`

2. **Hypothesize Instruction**: This instruction will guide the LLM to formulate a hypothesis based on the information gathered. If only a few bits of information are provided, the LLM will form a naive hypothesis. If background materials and previous hypotheses are provided, the LLM will revise the existing hypothesis. The output of this instruction is a string containing the formulated or revised hypothesis. This file is `system02_hypothesize.txt`

3. **Satisficing Check Instruction**: This instruction will guide the LLM to check if the information need has been satisficed. The LLM will observe all materials provided, including the original query, search results, hypotheses, and notes, and render a judgment. The output of this instruction is a JSON object containing feedback and a boolean indicating whether the information need has been satisficed. This file is `system03_satisficing_check.txt`
