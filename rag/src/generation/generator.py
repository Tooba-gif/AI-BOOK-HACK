import openai
from typing import List, Dict
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ..config.settings import settings

class Generator:
    def __init__(self):
        """
        Initialize the generator with OpenAI API key and model.
        """
        openai.api_key = settings.openai_api_key
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",  # Can be configured based on requirements
            temperature=0.3,  # Lower temperature for more consistent answers
            openai_api_key=settings.openai_api_key
        )
        
        # Define the prompt template for RAG
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an AI assistant for an AI Native Textbook on Physical AI & Humanoid Robotics. 
            Answer the user's question based ONLY on the provided textbook content. 
            If the information is not in the provided context, clearly state that the answer is not in the textbook.
            Always cite the specific chapters/sections where you found the information.
            Be concise but thorough in your responses."""),
            ("human", """Context information:
            {context}
            
            Question: {question}
            
            Answer:""")
        ])
        
        self.output_parser = StrOutputParser()
        self.chain = self.prompt | self.llm | self.output_parser
    
    def generate_answer(self, question: str, context: List[Dict]) -> str:
        """
        Generate an answer to the question based on the provided context.
        """
        # Format the context for the prompt
        context_str = "\n\n".join([
            f"Chapter: {item['section_title']}\nContent: {item['content'][:500]}..."  # Limit content length
            for item in context
        ])
        
        # Generate the answer
        answer = self.chain.invoke({
            "context": context_str,
            "question": question
        })
        
        return answer
    
    def generate_answer_with_citations(self, question: str, context: List[Dict]) -> Dict:
        """
        Generate an answer with citations to the source material.
        """
        answer = self.generate_answer(question, context)
        
        # Extract citations from the context
        citations = [
            {
                "chapter_id": item["chapter_id"],
                "section_title": item["section_title"],
                "score": item["score"]
            }
            for item in context
        ]
        
        return {
            "answer": answer,
            "citations": citations
        }