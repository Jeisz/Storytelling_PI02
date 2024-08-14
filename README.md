# Storytelling_PI02
# Análisis de Acceso a Internet en Argentina

## Descripción del Proyecto

Este proyecto analiza el acceso a diferentes tecnologías de internet en Argentina, utilizando diversos conjuntos de datos que incluyen acceso por provincias, penetración por hogares, y otros indicadores clave. El análisis se realiza a través de un dashboard interactivo creado con Streamlit, que permite explorar los datos de manera visual y dinámica.

## Storytelling del Análisis

### 1. **Introducción al Contexto**
   Argentina, como muchos países en desarrollo, enfrenta desafíos significativos en términos de acceso a internet. Este proyecto busca entender cómo las diferentes provincias y localidades del país están conectadas a internet y qué tecnologías son las más prevalentes. Además, se analiza la penetración de internet por cada 100 habitantes y hogares, con el objetivo de identificar brechas y oportunidades de mejora.

### 2. **Análisis de Accesos por Tecnología**
   - **Objetivo:** Examinar cómo se distribuyen las diferentes tecnologías de acceso a internet (ADSL, Cablemódem, Fibra óptica, Wireless, y otras) en las distintas provincias de Argentina.
   - **Visualización:** Se presenta un gráfico de barras que muestra el número de accesos por tecnología para cada provincia seleccionada y un año específico.
   - **Hallazgos Clave:** Identificación de provincias con baja adopción de tecnologías avanzadas como la fibra óptica, lo que sugiere áreas prioritarias para la mejora de infraestructura.

### 3. **Penetración de Internet por Hogares**
   - **Objetivo:** Evaluar el nivel de penetración de internet en los hogares de cada provincia.
   - **Visualización:** Un gráfico de barras interactivo que muestra los accesos por cada 100 hogares en las provincias seleccionadas.
   - **Hallazgos Clave:** Se observa una variabilidad significativa entre provincias, con algunas mostrando una alta penetración de internet, mientras que otras aún dependen de tecnologías más antiguas y menos eficientes.

### 4. **KPI de Aumento de Acceso a Internet**
   - **Objetivo:** Medir y visualizar el aumento del acceso a internet en términos porcentuales para cada trimestre.
   - **Visualización:** Gráfico de dispersión que muestra el KPI de aumento del acceso a internet por trimestre, destacando las provincias que han experimentado un crecimiento significativo.
   - **Hallazgos Clave:** Identificación de tendencias de crecimiento en el acceso a internet, destacando las provincias que han implementado políticas efectivas de expansión de internet.

### 5. **Mapa Interactivo de Conectividad**
   - **Objetivo:** Mostrar la distribución geográfica de las tecnologías de acceso a internet y otros indicadores de conectividad en las localidades de cada provincia.
   - **Visualización:** Un mapa interactivo creado con Folium, que permite a los usuarios explorar la conectividad de diferentes localidades en Argentina.
   - **Hallazgos Clave:** El mapa revela concentraciones de conectividad en áreas urbanas y regiones con infraestructuras más desarrolladas, mientras que las áreas rurales muestran una conectividad más limitada.

## Estructura del Proyecto

- `dep.py`: El script principal de Streamlit que genera el dashboard interactivo.
- `accesos_tecnologia.csv`: Dataset que contiene los datos de acceso a internet por tecnología.
- `penetracion_hogares.csv`: Dataset que muestra la penetración de internet por hogares en cada provincia.
- `kpi_aumento_acceso_internet.csv`: Dataset que incluye los KPIs de aumento de acceso a internet.
- `mapa_conectividad.xlsx`: Archivo Excel con datos de conectividad y coordenadas geográficas para las localidades de Argentina.

## Requisitos del Proyecto

Para ejecutar el proyecto, necesitas tener instaladas las siguientes dependencias:

```bash
pip install -r requirements.txt
