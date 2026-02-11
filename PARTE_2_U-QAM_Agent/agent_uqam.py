import os
import asyncio
from dotenv import load_dotenv

# Componentes de Google ADK
from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner

# Plugins y módulos auxiliares
from google.adk.plugins.logging_plugin import LoggingPlugin
from metrics_w_example import compute_metrics
from count_invocation_plugin import CountInvocationPlugin

load_dotenv()

# Configuración de reintentos para estabilidad de la API
retry_config = types.HttpRetryOptions(
    attempts=3,
    exp_base=2,
    initial_delay=1,
    http_status_codes=[429, 500, 503],
)

# ---------------------------------------------------------
# 1. DEFINICIÓN DE LA TOOL
# ---------------------------------------------------------

def analyze_text_quality(text: str) -> dict:
    """
    Calcula métricas objetivas de calidad de redacción para un texto dado.
    
    Args:
        text: El texto completo a analizar.
        
    Returns:
        Diccionario con métricas: LMO, INFLESZ, % Pasiva, Z-Score.
    """
    try:
        # Cálculo de métricas utilizando el módulo auxiliar
        metrics = compute_metrics(text)
        
        # Estructuración de la respuesta para el agente
        return {
            "status": "success",
            "metrics": {
                "num_sentences": metrics.num_sentences,
                "num_words": metrics.num_words,
                "LMO_mean_sentence_length": round(metrics.lmo, 2),
                "variability_cv": round(metrics.cv_sentence_len, 2),
                "z_normality_score": round(metrics.z_normality, 2),
                "inflesz_readability": round(metrics.flesch_szigriszt, 2),
                "passive_voice_ratio": round(metrics.passive_ratio, 2)
            }
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

print("✅ Tool 'analyze_text_quality' configurada.")


# ---------------------------------------------------------
# 2. CONFIGURACIÓN DEL AGENTE
# ---------------------------------------------------------

# Definición de la rúbrica de evaluación U-QAM (Opción Equilibrada)
uqam_instruction = """
You are the U-QAM Evaluator, an expert in text quality analysis.
Your goal is to calculate a final quality score (0-100) based on objective metrics.

PROTOCOL:
1. Receive the text from the user.
2. Use the tool `analyze_text_quality` to extract technical metrics.
3. Analyze the metrics based on the "Balanced U-QAM" Rubric below:

   --- U-QAM SCORING RUBRIC (Max 100 pts) ---
   
   A. READABILITY (INFLESZ) - Max 30 pts
      - Target: 55-75 (Normal/Easy). 
      - If in range: 30 pts.
      - If 40-54 (Hard) or >80 (Too simple): 15 pts.
      - Else: 5 pts.

   B. STRUCTURE (Z-Score Normality) - Max 30 pts
      - Target: -1.0 to +1.0.
      - If in range: 30 pts.
      - If between 1.0 and 2.0 (or -1.0 to -2.0): 15 pts.
      - Else: 5 pts.

   C. STYLE (Passive Voice) - Max 20 pts
      - Target: < 15%.
      - If < 15%: 20 pts.
      - If 15% - 25%: 10 pts.
      - Else: 0 pts.

   D. NATURALNESS (Variability CV) - Max 20 pts
      - Target: 0.5 - 1.0.
      - If in range: 20 pts.
      - Else: 10 pts.

OUTPUT FORMAT:
First, calculate the score step-by-step.
Then, provide the final report in Markdown:
# U-QAM Report
* **Final Score:** [Total Score]/100
* **Analysis:**
  * Readability: [Val] (Score: X/30) - [Comment]
  * Structure: [Val] (Score: X/30) - [Comment]
  * Passive Voice: [Val]% (Score: X/20) - [Comment]
  * Variability: [Val] (Score: X/20) - [Comment]
* **Conclusion:** Brief qualitative summary.
"""

uqam_agent = LlmAgent(
    name="uqam_evaluator",
    model=Gemini(
        model="gemini-2.5-flash-lite", 
        api_key=os.getenv("GOOGLE_API_KEY"),
        retry_options=retry_config
    ),
    instruction=uqam_instruction,
    tools=[analyze_text_quality]
)

# ---------------------------------------------------------
# 3. EJECUCIÓN
# ---------------------------------------------------------

if __name__ == "__main__":
    
    # Muestra 1: Texto Técnico (Referencia: Computación Cuántica)
    text_tech = """
    La computación cuántica es un paradigma de computación distinto al de la informática clásica. 
    Se basa en el uso de cúbits, una especial combinación de unos y ceros. Los bits de la computación 
    clásica pueden estar en 1 o en 0, pero solo un estado a la vez; en tanto el cúbit puede tener los 
    dos estados simultáneamente gracias a la superposición cuántica. Esto da lugar a nuevas puertas 
    lógicas que hacen posibles nuevos algoritmos. Una de las principales diferencias es que la computación 
    clásica es determinista, mientras que la cuántica es probabilística. Debido a su naturaleza, los 
    ordenadores cuánticos no son versiones más potentes de los ordenadores actuales, sino que son dispositivos 
    capaces de realizar operaciones que, para un ordenador tradicional, serían inviables por la cantidad de 
    recursos temporales necesarios.
    """

    # Muestra 2: Texto Literario (Referencia: Don Quijote)
    text_lit = """
    En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los 
    de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, 
    salpicón las más noches, duelos y quebrantos los sábados, lantejas los viernes, algún palomino de añadidura 
    los domingos, consumían las tres partes de su hacienda. El resto della concluían sayo de velarte, calzas de 
    velludo para las fiestas, con sus pantuflos de lo mismo, y los días de entresemana se honraba con su 
    vellorí de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba 
    a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera.
    """

    # Muestra 3: Texto Histórico (Referencia: Revolución Industrial)
    text_hist = """
    La Revolución Industrial marca un punto de inflexión en la historia, modificando e influenciando todos los 
    aspectos de la vida cotidiana de una u otra manera. La producción tanto agrícola como de la naciente 
    industria se multiplicó a la vez que disminuía el tiempo de producción. A partir de 1800 la riqueza y la 
    renta per cápita se multiplicó como no lo había hecho nunca en la historia, pues hasta entonces el PIB per 
    cápita se había mantenido prácticamente estancado durante siglos. En palabras del premio Nobel Robert Lucas: 
    Cita: por primera vez en la historia, el nivel de vida de las masas y la gente común experimentó un 
    crecimiento sostenido (...) No hay nada remotamente parecido a este comportamiento de la economía en ningún 
    momento del pasado.
    """

    texts = {
        "TÉCNICO": text_tech,
        "LITERARIO": text_lit,
        "HISTÓRICO": text_hist
    }

    async def main():
        # Inicialización de plugins de observabilidad
        logging_plugin = LoggingPlugin()
        efficiency_plugin = CountInvocationPlugin()
        
        runner = InMemoryRunner(
            agent=uqam_agent,
            plugins=[logging_plugin, efficiency_plugin]
        )

        print("\n🚀 INICIANDO BATERÍA DE PRUEBAS U-QAM\n" + "="*40)

        for category, text in texts.items():
            print(f"\n📄 Analizando texto: {category}...")
            print("-" * 20)
            
            # Ejecución del prompt de análisis
            await runner.run_debug(f"Analyze the following text and give me the U-QAM Score: {text}")
            
            print(f"\n✅ Fin análisis {category}.\n")

    asyncio.run(main())