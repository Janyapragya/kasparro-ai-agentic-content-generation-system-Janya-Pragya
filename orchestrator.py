
from agents.parser_agent import ParserAgent
from agents.question_agent import QuestionAgent
from agents.faq_agent import FAQAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent
import json

class Orchestrator:

    def run(self):
        product = ParserAgent().parse('data/product.json')

        questions = QuestionAgent().generate(product)
        faq = FAQAgent().make_faq(questions, product)
        json.dump({'faq': faq}, open('output/faq.json', 'w'), indent=2)

        page = ProductPageAgent().make_page(product)
        json.dump(page, open('output/product_page.json', 'w'), indent=2)

        comp = ComparisonAgent().compare(product)
        json.dump(comp, open('output/comparison_page.json', 'w'), indent=2)

        print('Generated all pages!')
