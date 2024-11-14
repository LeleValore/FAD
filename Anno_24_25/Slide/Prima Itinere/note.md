# Fondamenti di Analisi Dati - Appunti

## Basic Concepts

- **Dati**: I dati sono un insieme di valori raccolti rispetto ad alcune variabili che descrivono un determinato fenomeno. 

- **Osservazione**: Un osservazione è l'unità con la quale misuriamo il dato. Ad esempio: persone, macchine, animali, piante ecc. 

- **Popolazione**: La popolazione è l'insieme di osservazioni. Spesso l'insieme è solo teorico e non può essere ottenuto. 

- **Campione**: Un sottoinsieme della popolazione. Spesso non è possible trattare l'intera popolazione, quindi si lavora con un campione.

- **Variabile**: Una variabile è una caratteristica misurabile che può assumere diversi valori. Le variabili possono essere di due tipi:
  - **Variabili qualitative (categoriali)**: Variabili che rappresentano categorie o classi. Ad esempio: sesso, colore, stato civile ecc.

  - **Variabili quantitative**: Variabili che rappresentano quantità numeriche. Ad esempio: altezza, peso, reddito ecc.

- **Scale**: Le scale sono le modalità con cui le variabili possono essere misurate. Esistono quattro tipi di scale:
  - **Scala nominale**: Scala che rappresenta categorie per le quali non è possibile (o non ha senso) stabilire un'ordine. Ad esempio: sesso, colore degli occhi ecc.
  - **Scala ordinale**: Scala che rappresenta categorie ordinabili ma per le quali la differenza tra un livello ed un altro non è significativa. Ad esempio: livello di soddisfazione, livello di istruzione ecc.
  - **Scala continua**: Scala che rappresenta valori numerici. Ad esempio: altezza, peso, reddito ecc.

## Analisi dati
L'analisi dei dati è un processo di ispezione, pulizia, trasformazione e modellazione di dati con il fine di evidenziare informazioni che suggeriscano conclusioni e supportino le decisioni strategiche aziendali.

- **Ispezione**: analisi dei dati a disposizione e delle loro caratteristiche.
- **Pulizia**: rimozione di dati mancanti, ridondanti o errati.
- **Trasformazione**: conversione dei dati in un formato più adatto all'analisi, ad esempio normalizzazione.
- **Modellazione**: applicazione di tecniche statistiche e algoritmi di machine learning per estrarre informazioni utili.

___

## Variabili Aleatorie

- **Variabile Aleatoria** : Variabile il cui valore dipende da un evento stocastico. Una variabile aleatoria è una funzione che associa ad ogni esito di un esperimento casuale un valore numerico.

$$X: \Omega \rightarrow R$$

  Distinguiamo due tipi di variabili aleatorie:

  - Variabile casuale discreta: Variabile aleatoria che può assumere un numero finito o infinito numerabile di valori.

  - Variabile casuale continua: Variabile aleatoria che può assumere un numero infinito non numerabile di valori.

Risulta possibile ridefinire il dato come segue:

- **Dato**: Valore osservato di una variabile aleatoria.
___
## Probabilità

Introdurre la teoria della probabilità significa introdurre un modello matematico che permette di descrivere e studiare fenomeni aleatori.

### Definizione Laplaciana

Rappresenta la probabilità di un evento in funzione del numero di esiti favorevoli e del numero di esiti possibili.

$$P(A) = \frac{|A|}{|\Omega|} = \frac{\text{numero di esiti favorevoli}}{\text{numero di esiti possibili}}$$

### Definizione Frequentista

Rappresenta la probabilità di un evento in base a esperimenti ripetuti. Si considera la frequenza relativa di un evento.

$$P(A) = \frac{\text{numero di esiti favorevoli}}{\text{numero di esperimenti effettuati}}$$

### Definizione Bayesiana

Rappresenta la probabilità di un evento in base a conoscenze pregresse.

___

### Frequenza assoluta

Si definisce frequenza assoluta di un evento $A$ il numero di volte in cui l'evento si è verificato.

### Frequenza relativa

Si definisce frequenza relativa di un evento $A$ il rapporto tra la frequenza assoluta e il numero totale di esperimenti.

### Probabilità marginale (frequenza marginale)

La probabilità marginale di un evento $A$ è la probabilità che l'evento si verifichi indipendentemente dagli altri eventi. 

$$P(X=x_i) = \frac{n_{i+}}{n}$$ 
dove $n_{i+} = \sum_{j} n_{ij}$

$$P(Y=y_j) = \frac{n_{+j}}{n}$$
dove $n_{+j} = \sum_{i} n_{ij}$

### Probabilità congiunta

La probabilità congiunta di due eventi $X=x_i$ e $Y=y_j$ è la probabilità che entrambi gli eventi si verifichino contemporaneamente.

$$P(X=x_i, Y=y_i) = \frac{n_{ij}}{n}$$

Se $X$ e $Y$ sono indipendenti:

$$P(X=x_i, Y=y_j) = P(X=x_i) P(Y=y_j)$$

### Regola della somma o Marginalizzazione

Permette di calcolare la probabilità marginale di una variabile sommando le probabilità congiunte di tutte le possibili combinazioni di valori della variabile stessa con l'altra variabile.
$$P(X=x_i) = \sum_{j} P(X=x_i, Y=y_j)$$

### Regola del prodotto o Fattorizzazione

Permette di calcolare la probabilità congiunta di due variabili come il prodotto della probabilità condizionata di una variabile rispetto all'altra per la probabilità marginale dell'altra variabile.
$$P(X=x_i, Y=y_j) = P(X=x_i | Y=y_j) P(Y=y_j)$$

### Probabilità condizionata

La probabilità condizionata di un evento $X=x_i$ rispetto a un evento $Y=y_j$ è la probabilità che l'evento $X=x_i$ si verifichi sapendo che l'evento $Y=y_j$ si è verificato.

$$P(X=x_i | Y=y_j) = \frac{P(X=x_i, Y=y_j)}{P(Y=y_j)} = \frac{n_{ij}}{n_{+j}}$$

Se $X$ e $Y$ sono indipendenti:

$$P(X=x_i | Y=y_j) = P(X=x_i)$$

### Chain rule delle probabilità condizionate

$$P(X, Y, Z) = P(X | Y, Z) P(Y | Z) P(Z)$$

### Teorema di Bayes

Permette di calcolare la probabilità condizionata di un evento $Y$ rispetto a un evento $X$ conoscendo la probabilità condizionata di $X$ rispetto a $Y$, noto come verosimiglianza.

$$P(Y|X) = \frac{P(X|Y)P(Y)}{P(X)}$$

dove:

- $P(Y|X)$ è la probabilità a posteriori
- $P(X|Y)$ è la verosimiglianza, ovvero quanto bene un certo valore dei parametri spiega i dati osservati.
- $P(Y)$ è la probabilità a priori
- $P(X)$ è l'evidenza

___
## Distribuzioni di probabilità

Una distribuzione di probabilità è una funzione che assegna a ciascun evento un valore che rappresenta la probabilità che l'evento si verifichi.

$$P(X=x) = p$$

Se $X$ è una variabile aleatoria che segue una distribuzione di probabilità $P$, diremo che $X$ è distribuita come $P$ e scriveremo:
$$X \sim P$$

### PMF (Probability Mass Function)

Rappresenta la probabilità che una variabile casuale discreta $X$ assuma un determinato valore $x$.
$$P(X=x) = P(x)  \quad \text{con} \sum_{x} P(x) = 1$$

### PDF (Probability Density Function)

Rappresenta la probabilità che una variabile casuale continua $X$ assuma un valore compreso tra $a$ e $b$.
$$P(a \leq X \leq b) = \int_{a}^{b} f(x) \, dx \quad \text{con} \int_{-\infty}^{+\infty} f(x) \, dx = 1$$
dove $f(x)$ è la derivata della funzione di ripartizione $F(x)$.

### CDF (Cumulative Distribution Function)

Rappresenta la probabilità che una variabile casuale $X$ assuma un valore minore o uguale a $x$.
$$ \text{Variabile discreta:} \quad F(x) = P(X \leq x) = \sum_{x} P(x)$$
$$ \text{Variabile continua:} \quad F(x) = \int_{-\infty}^{x} f(t) \, dt$$
$$ \text{ex.} \quad P(a \leq X \leq b) = F(b) - F(a)$$

### Expectation

L'aspettazione di una variabile casuale è il valore atteso che ci si aspetta di ottenere dalla variabile se si ripete l'esperimento un numero infinito di volte e si calcola la media dei risultati.
$$\text{Variabile discreta}: \quad E[X] = \sum_{x \in X} x P(x)$$
$$\text{Variabile continua}: \quad E[X] = \int_{-\infty}^{+\infty} x f(x) \, dx$$

### Variance

La varianza di una variabile casuale è lo scarto quadratico medio tra i valori della variabile e la media. Rappresenta la dispersione dei dati attorno alla media.
$$Var[X] = E[(X - E[X])^2] = E[X^2] - E[X]^2$$

### Standard deviation

La deviazione standard di una variabile casuale è la radice quadrata della sua varianza.
$$\sigma = \sqrt{Var[X]}$$

### Covariance

La covarianza tra due variabili $X$ e $Y$ è una misura della relazione lineare tra le due variabili. Se la covarianza è positiva, allora i valori di $X$ e $Y$ tendono ad aumentare insieme. Se la covarianza è negativa, allora i valori di $X$ tendono ad aumentare mentre i valori di $Y$ tendono a diminuire.
$$Cov[X, Y] = E[(X - E[X])(Y - E[Y])]$$

#### Matrice di covarianza

$$\Sigma = 
\begin{bmatrix} 
\sigma^2_x & \sigma_{xy} \\ 
\sigma_{yx} & \sigma^2_y 
\end{bmatrix}$$

### Standardizzazione

$$Z = \frac{X - E[X]}{\sqrt{Var[X]}}$$

### Distribuzioni discrete

#### Bernoulli
$$P(X=1) = p \quad P(X=0) = 1-p$$

#### Binomiale
$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$

#### Uniforme
$$P(X=a_i) = \frac{1}{k} \quad k \in N$$
con $a_i \in \{a_1, a_2, \ldots, a_k\}$

#### Multinoulli o Categorica
$$P(X=a_i) = p_i \quad \text{con} \sum_{i} p_i = 1$$

#### Multinomiale
$$P(X=n1, \ldots, n_k) = \frac{n!}{n_1! n_2! \ldots n_k!} p_1^{n_1} p_2^{n_2} \ldots p_k^{n_k}$$

### Distribuzioni continue

#### Gaussiana o Normale
$$N(x, \mu, \sigma^2) = \sqrt{\frac{1}{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$
dove $\mu \in R$ è la media e $\sigma \in R^+$ è la deviazione standard. 

**Regola empirica**:

- $68\%$ dei dati si trova entro $1\sigma$ dalla media
- $95\%$ dei dati si trova entro $2\sigma$ dalla media
- $99.7\%$ dei dati si trova entro $3\sigma$ dalla media

### Interpretazione della Gaussiana 

- **Termine di normalizzazione**:
$$
\frac{1}{\sqrt{2 \pi \sigma^2}}
$$
è un termine di normalizzazione che assicura che l'integrale della funzione di densità su tutto l'asse reale sia pari a 1. Ciò è fondamentale affinché la distribuzione possa essere considerata valida come funzione di probabilità.

- **Massimo della distribuzione**:
Quando $ x = \mu $, l'esponenziale diventa 1, e quindi il termine di normalizzazione $\frac{1}{\sqrt{2 \pi \sigma^2}}$ rappresenta il valore massimo della distribuzione, che si verifica proprio alla media.

- **Simmetria rispetto alla media**:
Il termine quadratico $(x - \mu)^2$ garantisce la simmetria della distribuzione rispetto alla media $\mu$. Questa simmetria implica che le probabilità di osservare valori ugualmente distanti dalla media siano le stesse, sia a sinistra che a destra.

- **Effetto della deviazione standard**:
La presenza del termine $\sigma^2$ nel denominatore del termine esponenziale indica che, all'aumentare della dispersione dei dati (cioè, all'aumentare di $\sigma$), la forma della distribuzione tende a "spanciarsi" e a ridurre l'altezza della campana. Questo comportamento implica che i dati sono più dispersi attorno alla media, rendendo la distribuzione meno concentrata.

#### Media
$$\hat{\mu} = \frac{1}{n} \sum_{i} x_i$$

#### Deviazione standard
$$\hat{\sigma}^2 = \frac{1}{n} \sum_{i} (x_i - \hat{\mu})^2$$

#### Gaussiana Multivariata

$$N(\bar{x}, \bar{\mu}, \Sigma) = \frac{1}{(2\pi)^{d/2} |\Sigma|^{1/2}} e^{-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)}$$
$\text{con} \quad \Sigma \quad \text{positiva definit}a$

### T-Student

$$t = \frac{\bar{x} - \mu}{s/\sqrt{n}}$$

dove :
- $s$ è la deviazione standard campionaria
- $\bar{x}$ è la media campionaria
- $\mu$ è la media della popolazione
- $n$ è la dimensione del campione

___
## Teoria dell'informazione

L'informazione è qualsiasi dato che mi permette di avere conoscenza, più o meno esatta, su un fenomeno. Introduciamo la teoria dell'informazione perchè siamo interessati a capire quanto sia informativa una variabile casuale.

### Self-information

$$I(x) = -\log P(x)$$

$$I(X=x, Y=y) = -\log P(X=x, Y=y)$$

### Entropia di Shannon

$$H(X) = E[I(x)] = -E[\log P(x)]$$
$$ \text{Variabile discreta:} \quad H(X) = -\sum_{x} P(x) \log P(x)$$
$$ \text{Variabile continua:} \quad H(X) = -\int_{-\infty}^{+\infty} f(x) \log f(x) \, dx$$
___

## Grafici

### Grafico a barre

- **Quando utilizzarlo**: 
  - Visualizzazione di categorie discrete, utile per mostrare distribuzioni di frequenze o confrontare categorie.
  
- **Come interpretarlo**: 
  - Le barre rappresentano categorie, la loro altezza o lunghezza indica la frequenza o il valore della categoria.

### Istogramma

- Tipi: 
  - Istogramma non normalizzato: Mostra le frequenze assolute per intervallo.
  - Istogramma normalizzato: Mostra le frequenze relative per intervallo. Ottenuto dividendo il valore dell'area di ogni bin per il totale delle frequenze.
  - Istogramma di densità: Stima della densità di probabilità. Ottenuto dividendo il valore dell'area di ogni bin per il prodotto tra il totale delle frequenze e la larghezza del bin.

- Quando utilizzarlo: 
  - Visualizzare la distribuzione di una variabile continua, suddivisa in intervalli.

- Come interpretarlo: 
  - L'asse orizzontale rappresenta intervalli di valori, l'asse verticale rappresenta la frequenza o densità.

### Grafico a torta

- Quando utilizzarlo: 
  - Visualizzare la distribuzione di una variabile categorica e quindi non ordinabile in maniera naturale.

### Boxplot

- Quando utilizzarlo: 
  - Visualizzare la distribuzione di una variabile continua, utile per mostrare la presenza di outliers e la distribuzione dei dati.

- Come interpretarlo:
  - La linea centrale rappresenta la mediana, la parte centrale del box rappresenta il primo e terzo quartile, i baffi rappresentano il range interquartile, i punti rappresentano gli outliers.

### Scatter plot

- Quando utilizzarlo: 
  - Visualizzare la relazione tra due variabili continue.

- Come interpretarlo:
  - Ogni punto rappresenta una coppia di valori, l'asse x e y rappresentano le variabili in esame.

### Heatmap

- Quando utilizzarlo: 
  - Visualizzare la relazione tra due variabili categoriche.

- Come interpretarlo:
  - Le celle colorate rappresentano la frequenza o il valore della relazione tra le due variabili.

___
## Misure di Tendenza Centrale

### Media 

$$\bar{X} = \frac{1}{N} \sum_{i}{x_i}$$

- Significato: Valore calcolato come la somma di tutti i valori diviso il numero di valori.

### Mediana

- Significato: Valore centrale di un insieme di dati ordinati che li divide in due parti di uguale cardinalità.

### Quantili

- Significato: Il quantile di ordine $\alpha$ è il valore $q_\alpha$ che divide la distribuzione in due parti, in modo che la probabilità che un campione casuale sia minore o uguale a $q_\alpha$ sia $\alpha$.

### Percentili

- Significato: Il percentile di ordine $\alpha$ è il valore percentuale $q_\alpha$ che divide la distribuzione in due parti, in modo che la probabilità che un campione casuale sia minore o uguale a $q_\alpha$ sia $\alpha$ percento.

### Quartili

- Significato: I quartili sono i tre valori che dividono la distribuzione in quattro parti uguali. 

    - Quartile di ordine 0: Minimo
    - Quartile di ordine 1: 25° percentile
    - Quartile di ordine 2: 50° percentile (mediana)
    - Quartile di ordine 3: 75° percentile
    - Quartile di ordine 4: Massimo

### Moda

- Significato: Valore che compare più frequentemente in un insieme di dati.

___
## Misure di Dispersione e Forma

### Minimo, Massimo e Range (indicatori non robusti alla presenza di outliers)

- Significato: Valore minimo e massimo di un insieme di dati. Il range è la differenza tra il massimo e il minimo.

### Distanza Interquartile (IQR) (indicatore robusto alla presenza di outliers)

- Significato: Misura di dispersione che indica la differenza tra il terzo e il primo quartile. Ad esempio, se l'IQR è piccolo, i dati sono concentrati attorno alla mediana. Se l'IQR è grande, i dati sono più dispersi.

### Deviazione Standard e Varianza (indicatori robusti alla presenza di outliers)

#### - Deviazione Standard

$$\sigma = \sqrt{\frac{1}{N} \sum_{i}{(x_i - \bar{X})^2}}$$

- Significato: Misura di dispersione che indica quanto i dati si discostano dalla media. Se i dati seguono una distribuzione normale, il $68\%$ dei dati si trova entro una deviazione standard dalla media.

#### - Varianza

$$\sigma^2 = \frac{1}{N} \sum_{i}{(x_i - \bar{X})^2}$$

- Significato: A differenza della deviazione standard, la varianza fornisce una misura più intuitiva della dispersione dei dati.

___
## Misure di Correlazione tra variabili discrete

### Statistica $\chi^2$ di Pearson 

$$\chi^2 = \sum_{i=1}^{k} \sum_{j=1}^{l} \frac{(n_{ij} - n^{\sim}_{ij})^2}{n^{\sim}_{ij}}$$

dove:
  - $n_{ij}$ è la probabilità congiunta osservata $P(X=x_i, Y=y_j)$
  - $n^{\sim}_{ij}$ è la probabilità congiunta attesa $P(X=x_i)P(Y=y_j)$
  - $k$ è il numero di categorie di $X$
  - $l$ è il numero di categorie di $Y$

Nel denominatore compare $ n^{\sim}_{ij} $, che serve a pesare maggiormente gli scarti nei casi in cui le frequenze attese sono grandi, e meno nei casi in cui sono piccole.

**Bound**: La statistica ha valori compresi tra 0 e $+\infty$.

**Interpretazione**: 

   - Se il valore della statistica $\chi^2$ è elevato, questo indica che c'è una discrepanza significativa tra i valori osservati e quelli attesi, suggerendo che le variabili in esame sono associate.
   
   - Un valore basso di $\chi^2$ suggerisce invece che i dati osservati sono vicini a quelli attesi, e quindi non vi è una forte evidenza di associazione tra le variabili.
___
### Statistica $V$ di Cramer 

$$V = \sqrt{\frac{\chi^2}{n \cdot \min(k-1, l-1)}}$$

**Bound**: La statistica $V$ di Cramer assume valori compresi tra 0 e 1.

**Interpretazione**: 

   - Se $V = 0$, allora le variabili sono scorrelate.
   - Se $V = 1$, allora le variabili sono correlate.
___
### Rischio Relativo 

Il RR dice quanto è più probabile che un evento si verifichi in un gruppo rispetto a un altro. Affidabile solo se il campione è rappresentativo della popolazione.

$$RR = \frac{P(X=1|Y=1)}{P(X=1|Y=0)}$$

dove: 
- $P(X=1|Y=1)$ è la probabilità di ossevare $X=1$ quando $Y=1$
- $P(X=1|Y=0)$ è la probabilità di ossevare $X=1$ quando $Y=0$

**Bound**: Il rischio relativo assume valori compresi tra 0 e $+\infty$.

**Interpretazione**: 
- Se $RR > 1$, allora la probabilità di avere $X=1$ è maggiore quando $Y=1$ rispetto a quando $Y=0$. 
- Se $RR = 1$, allora la probabilità di avere $X=1$ è la stessa quando $Y=1$ e quando $Y=0$.
- Se $RR < 1$, allora la probabilità di avere $X=1$ è minore quando $Y=1$ rispetto a quando $Y=0$.
___
### Odds Ratio

L'OR risulta affidabile anche se il campione non è rappresentativo della popolazione poichè nella formula vengono annullati i conteggi assoluti, ovvero i denomitatori degli odds.

$$OR = \frac{Odds(X=1|Y=1)}{Odds(X=1|Y=0)}$$

dove:
- $Odds(X=1|Y=1) = \frac{P(X=1|Y=1)}{1 - P(X=1|Y=1)}$
- $Odds(X=1|Y=0) = \frac{P(X=1|Y=0)}{1 - P(X=1|Y=0)}$

**Bound**: L'odds ratio assume valori compresi tra 0 e $+\infty$.

**Interpretazione**:

- Se $OR > 1$, allora la probabilità di avere $X=1$ è maggiore quando $Y=1$ rispetto a quando $Y=0$.
- Se $OR = 1$, allora la probabilità di avere $X=1$ è la stessa quando $Y=1$ e quando $Y=0$.
- Se $OR < 1$, allora la probabilità di avere $X=1$ è minore quando $Y=1$ rispetto a quando $Y=0$.

**NB: Se $X$ è un evento raro, si ha che OR = RR**
___
## Misure di Correlazione tra variabili continue

### Covarianza

$$Cov(X, Y) = \frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{X})(y_i - \bar{Y})$$

**Bound**: La covarianza assume valori compresi tra $-\infty$ e $+\infty$.

**Interpretazione**:

- Se la covarianza è positiva, allora i valori di $X$ e $Y$ tendono ad aumentare insieme.
- Se la covarianza è nulla, allora $X$ e $Y$ sono scorrelate.
- Se la covarianza è negativa, allora i valori di $X$ tendono ad aumentare mentre i valori di $Y$ tendono a diminuire.

Va anche notato che i valori della correlazione non sono normalizzati e dipendono dai range delle singole variabili, per cui non è possibile confrontare le covarianze.
___
### Coefficiente di correlazione di Pearson

$$\rho = \frac{Cov(X, Y)}{\sigma_X \sigma_Y}$$

dove:
- $\sigma_X$ e $\sigma_Y$ sono le deviazioni standard di $X$ e $Y$.

**Bound**: Il coefficiente di correlazione di Pearson assume valori compresi tra -1 e 1.

- Significato: Misura la forza e la direzione della relazione lineare tra due variabili.

**Interpretazione**:

- Se $\rho = 1$, allora c'è una correlazione positiva perfetta tra le variabili.
- Se $\rho = 0$, allora le variabili sono scorrelate.
- Se $\rho = -1$, allora c'è una correlazione negativa perfetta tra le variabili.
___
### Coefficiente di correlazione di Spearman per ranghi (correlazione non lineare) $\rightarrow$ Non chiede la formula

$$R = 1 - \frac{6 \sum_{i=1}^{N} d_i^2}{N(N^2 - 1)}$$

dove:
- $d_i$ è la differenza tra i ranghi delle variabili $X$ e $Y$.

Invece di ragionare sui punteggi individuali, l’indice di correlazione di Spearman ordina i prodotti per score e verifica se gli ordinamenti ottenuti sono simili.

**Bound**: Il coefficiente di correlazione di Spearman assume valori compresi tra -1 e 1.

**Significato**: Misura la forza e la direzione della relazione tra due variabili, ma non necessariamente lineare.

**Interpretazione**:

- Se $R = 1$, allora c'è una correlazione positiva perfetta tra i ranghi delle variabili.
- Se $R = 0$, allora i ranghi delle variabili sono scorrelati.
- Se $R = -1$, allora c'è una correlazione negativa perfetta tra i ranghi delle variabili.
___
## Statistica inferenziale

### Standard Error

$$SE = \frac{\sigma}{\sqrt{n}}$$

Nel caso di una distribuzione binomiale, la deviazione standard della media campionaria è data da:

$$SE(\hat{p}) = \frac{\sqrt{\hat{p}(1-\hat{p})}}{\sqrt{n}}$$

**Significato**: Misura la precisione di un campione rispetto alla popolazione. Più precisamente, indica quanto la media campionaria si discosta dalla media della popolazione.

### Deviazione Standard della media campionaria

$$\sigma(\hat{p}) = \frac{\sqrt{p(1-p)}}{\sqrt{n}}$$

**Significato**: Misura la dispersione delle medie campionarie attorno alla media della popolazione.

### Confidence Interval

$$CI = P(\hat{p}-\sigma(\hat{p}) \leq p \leq \hat{p}+\sigma(\hat{p})) = 0.683$$

Possiamo affermare, con una confidenza del $68.8%$ che la propabilità reale $p$ si trova nell'intervallo $[\hat{p}-\sigma(\hat{p}); \quad \hat{p}+\sigma(\hat{p})]$

Analogamente valgono le seguenti relazioni:

$$P(\hat{p}-\sigma(\hat{p}) \leq \quad p \quad \leq \hat{p}+\sigma(\hat{p})) = 0.683$$
$$P(\hat{p}-2\sigma(\hat{p}) \leq \quad p \quad \leq \hat{p}+2\sigma(\hat{p})) = 0.954$$
$$P(\hat{p}-3\sigma(\hat{p}) \leq \quad p \quad \leq \hat{p}+3\sigma(\hat{p})) = 0.997$$

**Differenza tra confidenza e significatività**:
- **Confidenza**: Indica quanto siamo sicuri che l'intervallo contenga il valore vero.
- **Significatività**: Indica quanto è improbabile che il valore vero sia fuori dall'intervallo.

### Stimatori non distorti
Un intervallo di confidenza per un parametro $ p $ è calcolato come:

$$
\text{Intervallo di Confidenza} = \left[\hat{p} - k \cdot \sigma(\hat{p}), \, \hat{p} + k \cdot \sigma(\hat{p}) \right]
$$

dove:
  - $\hat{p} $ è la stima empirica del parametro $ p $ ottenuta dal campione,
  - $k$ è un fattore di confidenza che determina quante deviazioni standard includere attorno a $ \hat{p} $ per coprire il livello di confidenza desiderato:

    - $k = 1 $ per un livello di confidenza del 68.3\%,

    - $k = 2 $ per un livello di confidenza del 95.4\%,

    - $k = 3 $ per un livello di confidenza del 99.7\%.

  - $\sigma(\hat{p}) $ è la deviazione standard della distribuzione dei campionamenti che stimano il parametro $p$, calcolata come:
  $\sigma(\hat{p}) = \sqrt{\frac{p (1 - p)}{n}}$

#### Stimatore non distorto della media

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

#### Stimatore non distorto della varianza

$$s^2_{n-1} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

### Statistica T-student 

$$t = \frac{\bar{x} - \mu}{s_{n-1}/\sqrt{n}}$$ 

dove:
- $\bar{x}$ è la media campionaria
- $\mu$ è la media della popolazione
- $s_{n-1}$ è lo stimatore non distorto della deviazione standard campionaria
- $n$ è la dimensione del campione

La distribuzione t-Student approssima una gaussiana, ma è più incerta di una gaussiana per piccoli valori di n.
___
## Test di ipotesi

- **Ipotesi nulla $H_0$**: Affermazione che si vuole rigettare.

- **Ipotesi alternativa $H_1$**: Affermazione che si vuole dimostrare.

- **Livello di significatività $\alpha$**: Probabilità di rigettare l'ipotesi nulla quando è vera.

- **p-value**: Probabilità di osservare un evento più estremo di quello osservato, se si fa un altro campionamento, assumendo che l'ipotesi nulla sia vera.
  $$P(|z| > |t|)$$
  dove:
  - $t$ è la statistica t di Student calcolata sul campione 
  - $z$ è la statistica t di Student calcolata su un successivo ipotetico campionamento.

- **Decisione**: 
  - Se $p \lt \alpha$, allora si rigetta l'ipotesi nulla.
  - Se $p \geq \alpha$, allora non si rigetta l'ipotesi nulla.
___
### Test di ipotesi per la media

$$H_0: \mu = \mu_0$$
$$H_1: \mu \neq \mu_0$$

dove:
$$t = \frac{\bar{x} - \mu}{s_{n-1}/\sqrt{n}}$$ 

Se $p_{-value} < \alpha$ allora si rigetta l'ipotesi nulla, ovvero si afferma che la media campionaria è significativamente diversa dalla media della popolazione.

**Esempio**:
Voglio testare se la media di un campione è diversa da 10. 

___
### Test $\chi^2$ d'indipendenza (Variabili categoriali)

Viene utilizzato per testare se due variabili categoriali sono indipendenti.

$$H_0: \text{Non c'è associazione significativa tra le variabili categoriali (sono indipendenti)}$$
$$H_1: \text{C'è associazione significativa tra le variabili categoriali (sono dipendenti)}$$

dove:
$$\chi^2 = \sum_{i=1}^{k} \sum_{j=1}^{l} \frac{(n_{ij} - n^{\sim}_{ij})^2}{n^{\sim}_{ij}}$$

Se $p_{-value} < \alpha$ allora si rigetta l'ipotesi nulla, ovvero si afferma che le variabili categoriali sono dipendenti.

**Esempio**:
Voglio testare se c'è una relazione tra il sesso e il fumo. Si ha che le variabili sono indipendenti se la probabilità di fumare è la stessa per uomini e donne.
___
### Test $\chi^2$ Goodness of Fit (Variabili categoriali) $\rightarrow$ Utilizzabile per Statistica $\chi^2$ di Pearson

Viene utilizzato per testare se le frequenze osservate di una variabile categoriale differiscono significativamente da una distribuzione di frequenza di riferiment.

$$H_0: \text{Non ci sono differenze significative tra le frequenze osservate e quelle attese (Sono uguali)}$$
$$H_1: \text{Ci sono differenze significative tra le frequenze osservate e quelle attese (Sono diverse)}$$

Se $p_{-value} < \alpha$ allora si rigetta l'ipotesi nulla, ovvero si afferma che i dati osservati non seguono la distribuzione attesa.

**Esempio**:
Per esempio voglio sapere se la distribuzione di un dado è equa, quindi mi aspetto che le frequenze osservate siano simili a quelle attese. Allora confronto le frequenze osservate con $1/6$ .
___
### Test di correlazione di Pearson/Spearman (Variabili continue)

Viene utilizzato per testare se due variabili quantitative continue e normalmente distribuite sono correlate.

$$H_0: \text{Non c'è correlazione significativa tra le variabili (sono indipendenti)}$$
$$H_1: \text{C'è correlazione significativa tra le variabili (sono dipendenti)}$$

dove:
$$\chi^2 = \sum_{i=1}^{k} \sum_{j=1}^{l} \frac{(n_{ij} - n^{\sim}_{ij})^2}{n^{\sim}_{ij}}$$

oppure:

$$R = 1 - \frac{6 \sum_{i=1}^{N} d_i^2}{N(N^2 - 1)}$$

Se $p_{-value} < \alpha$ allora si rigetta l'ipotesi nulla, ovvero si afferma che le variabili sono correlate.

**Esempio**:
Voglio testare se c'è una correlazione tra il peso e l'altezza di un campione di persone.

___
### Test di Shapiro-Wilk ($n\leq2000$)

Usato per testare se un campione segue una distribuzione normale. Il test risulta affidabile per campioni di al più 2000 osservazioni.

$$H_0: \text{Il campione segue una distribuzione normale}$$
$$H_1: \text{Il campione non segue una distribuzione normale}$$

Se $p_{-value} < \alpha$ allora si rigetta l'ipotesi nulla, ovvero si afferma che il campione non segue una distribuzione normale.
___
### Test $K^2$ di D'Agostino ($n\geq50$)

Questo test è basato su Skewness e Kurtosis e viene utilizzato per testare se un campione segue una distribuzione normale.

$$H_0: \text{Il campione segue una distribuzione normale}$$
$$H_1: \text{Il campione non segue una distribuzione normale}$$

Se $p_{-value} < \alpha$ allora si rigetta l'ipotesi nulla, ovvero si afferma che il campione non segue una distribuzione normale.

Si basa su Skeewness e Kurtosis, quindi è più affidabile per campioni di almeno 50 osservazioni.

- **Skewness**: Misura l'asimmetria della distribuzione. Se la skewness è 0, allora la distribuzione è simmetrica. Se la skewness è positiva, allora la distribuzione è più "spostata" verso sinistra rispetto a una normale. Se la skewness è negativa, allora la distribuzione è più "spostata" verso destra rispetto a una normale.

- **Kurtosis**: Misura la forma della distribuzione. Se la kurtosis è 0, allora la distribuzione ha la stessa forma di una distribuzione normale. Se la kurtosis è positiva, allora la distribuzione è più "appuntita" rispetto a una normale. Se la kurtosis è negativa, allora la distribuzione è più "piatta" rispetto a una normale.
___
## Regressione Lineare

### Regressione Lineare Semplice

$$Y = \beta_0 + \beta_1 X + \epsilon$$

Si richiede che gli errori $\epsilon$ siano indipendenti e normalmente distribuiti con media nulla e varianza costante, ovvero $\epsilon \sim N(0, \sigma^2)$.

- **Interpretazione geometrica dei coefficienti**:
  - $\beta_0$ è l'intercetta, ovvero il punto in cui la retta interseca l'asse delle ordinate. 
  - $\beta_1$ è il coefficiente angolare, ovvero l'inclinazione della retta rispetto all'asse delle ascisse.
  - $\epsilon$ è termine di errore che rappresenta la variabilità dei dati non spiegata dal modello lineare, catturando l'effetto di altri fattori e l'incertezza stocastica.

- **Interpretazione statistica dei coefficienti**:
  - $\beta_0$: Indica il valore di $Y$(mpg) quando $X=0$ (horsepower). Quindi in caso di indipenza da $X$, $\beta_0$ rappresenta il valore atteso di $Y$.
  - $\beta_1$: Indica è l'incrementto che mi aspetto di osservare in $Y$ (mpg) per un incremento di 1 unità in $X$ (horsepower).
  - $\epsilon$: la variazione in $Y$ non spiegata dalla relazione lineare tra $X$ e $Y$, includendo errori di misura, fattori non osservati e componenti casuali.

### Residual Sum Square (Loss Function)
$$RSS = e_1^2 + e_2^2 + \ldots + e_n^2 = \sum_{i=1}^{n} e_i^2$$

dove:

- $e_i = y_i - \beta_0 - \beta_1 x_i = y_i - \hat{y}_i$ è il residuo per l'osservazione $i$.

Si può quindi scrivere l'RSS come:
$$RSS(\beta_0, \beta_1) = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i)^2$$

### Standard Error di $\beta_0$ e $\beta_1$ $\rightarrow$ Non chiede la formula

Rappresenta una stima dell'incertezza associata alle stime di $\beta_0$ e $\beta_1$. In altre parole, il SE di un coefficiente indica quanto potrebbe variare la stima di quel coefficiente se ripetessimo il campionamento e ricalcolassimo la regressione su campioni diversi.

$$SE(\beta_0) = \sigma^2 \left[ \frac{1}{n} + \frac{\bar{x}^2}{\sum_{i=1}^{n}(x_i - \bar{x})^2} \right]$$
$$SE(\beta_1) = \frac{\sigma}{\sum_{i=1}^{n}(x_i - \hat{x})^2}$$

dove:
- $\sigma^2$ è la varianza degli errori $Var(\epsilon)$.

Si nota che $\sigma^2$ non è direttamente osservabile, ma possiamo stimarlo con il **residual standard error**:

$$RSE = \sqrt{\frac{RSS}{n-2}}$$

In questo senso lo standard error viene utilizzato come stimatore non distorto della deviazione standard della distribuzione dei coefficienti stimati. In altre parole, il SE fornisce una misura di quanto ci aspettiamo che le stime dei coefficienti 
$\beta_0$ e $\beta_1$ possano variare attorno ai loro valori veri.

L'interpretazione di RSE ha senso solo in funzione dei valori della scala di $Y%$. Sia $\bar{y}$ la media di $Y$, allora l'errore percentuale sarà $\frac{RSE}{\bar{y}}$ %.
___
### Test statistico per la significatività dei coefficienti

Si vuole impostare un test per verificare se il coefficiente $\beta_1$ è significativamente diverso da zero.  
Nel caso in cui $\beta_1$ non sia significativamente diverso da zero, diremo che $X$ e $Y$ sono variabili indipendenti, ovvero $Y$ non può essere predetta da $X$ poiché non sono correlate.

$$H_0: \text{ Non c'è associazione tra } X \text{ e } Y \Leftrightarrow \beta_1 = 0$$
$$H_1: \text{ C'è un'associazione tra } X \text{ e } Y \Leftrightarrow \beta_1 \neq 0$$

dove:
$$t = \frac{\hat{\beta}_1 - 0}{SE(\hat{\beta}_1)}$$

Se $p_{-value} < \alpha$ allora si rigetta l'ipotesi nulla, ovvero si afferma che il coefficiente $\beta_1$ è significativamente diverso da zero, quindi esiste una correlazione tra $X$ e $Y$.

___

### Esempi di output di una regressione lineare

Sia $Y=mpg$ e $X=horsepower$, un possibile output di una regressione lineare potrebbe essere:

<table>
    <tr>
        <th></th>
        <th>COEFFICIENT</th>
        <th>STD ERROR</th>
        <th>t</th>
        <th>P-value</th>
        <th>CONFIDENCE INTERVAL</th>
    </tr>
    <tr>
        <td>&beta;<sub>0</sub></td>
        <td>39.94</td>
        <td>0.717</td>
        <td>55.66</td>
        <td>0</td>
        <td>[38.53, 41.35]</td>
    </tr>
    <tr>
        <td>&beta;<sub>1</sub></td>
        <td>-0.1578</td>
        <td>0.006</td>
        <td>-24.49</td>
        <td>0</td>
        <td>[-0.17, -0.15]</td>
    </tr>
</table>

### Analisi

- Coefficienti
  - Il coefficiente di $\beta_0$ è 39.94, il che significa che ci aspettiamo che il valore di $mpg$ sia 39.94 quando $horsepower=0$.
  - Il coefficiente di $\beta_1$ è -0.1578, il che significa che ci aspettiamo che il valore di $mpg$ diminuisca di 0.1578 unità per ogni unità di aumento di $horsepower$ (sono inversamente proporzionali).

- Standard Error (incertezza)
  - Lo standard error di $\beta_0$ è 0.717, il che significa che ci aspettiamo che la stima di $\beta_0$ vari di 0.717 unità se ripetiamo il campionamento.
  - Lo standard error di $\beta_1$ è 0.006, il che significa che ci aspettiamo che la stima di $\beta_1$ vari di 0.006 unità se ripetiamo il campionamento.

- Test di significatività
  - Il p-value per $\beta_0$ e $\beta_1$ è 0, il che significa che possiamo rigettare l'ipotesi nulla e affermare che i coefficienti sono significativamente diversi da zero.

- Confidence Interval
  - Il confidence interval per $\beta_0$ è [38.53, 41.35], il che significa che siamo sicuri al 95% che il valore vero di $\beta_0$ si trovi in questo intervallo.
  - Il confidence interval per $\beta_1$ è [-0.17, -0.15], il che significa che siamo sicuri al 95% che il valore vero di $\beta_1$ si trovi in questo intervallo.

___

### Valutazione della bontà del modello

Si pensa di assumere come baseline un modello che assume l'assenza di correlazione tra $X$ ed $Y$ del tipo:

$$Y = k$$

dove $k$ è una costante. In caso di indipendenza tra $X$ ed $Y$ si ha che il best $k$ è la media di $Y$, ovvero $k = \bar{y}$. 

### Total Sum of Squares (TSS)

Rappresenta la variabilità totale dei dati rispetto alla media, quindi il massimo di varianza che è possibile spiegare.

$$TSS = \sum_{i=1}^{n} (y_i - \bar{y})^2$$

dove:
- $y_i$ è il valore osservato di $Y$
- $\bar{y}$ è la media di $Y$

### Statistica $R^2$ 

$$R^2 = 1 - \frac{RSS}{TSS}$$

**Significato**: offre un'indicazione diretta di quanto bene il modello riesca a spiegare la variabilità nei dati, rispetto a un modello che non fa alcuna assunzione di correlazione.

Si nota che $R^2$ misura la proporzione di varianza spiegata dal modello rispetto ad un modello che non assume relazione tra le variabili.

**Interpretazione**:

-  Se $R^2 = 1$, allora il modello spiega perfettamente la variazione di $Y$.
-  Se $R^2 = 0$, allora il modello non spiega la variazione di $Y$.

Se ad esempio $R^2 = 0.8$, allora il modello riesce a spiegare l'80% della varianza dei dati.

**Nota**: $R^2$ alto non implica necessariamente che il modello sia buono, in quanto potrebbe essere dovuto ad un overfitting del modello.
___

## Regressione Lineare Multipla

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \ldots + \beta_n X_n + \epsilon$$

- **Interpretazione geometrica dei coefficienti**:
  - $\beta_0$ è l'intercetta, ovvero il punto in cui il piano interseca l'asse delle ordinate.
  - $\beta_1, \beta_2, \ldots, \beta_n$ sono i coefficienti angolari, ovvero l'inclinazione del piano rispetto agli assi delle ascisse.

- **Interpretazione statistica dei coefficienti**:
  - $\beta_0$: Indica il valore atteso di $Y$ quando tutte le alte $X_i$ sono poste a zero.
  - $\beta_1, \beta_2, \ldots, \beta_n$: Indicano l'incremento di $Y$ che si osserva quando $X_i$ aumenta di una unità, assumendo che tutti gli altri $X_j$ siano costanti.

- **Interpretazione di causa-effetto dei coefficienti**:
  - $\beta_1, \beta_2, \ldots, \beta_n$: Indicano l'effetto di una variazione di una unità di $X_i$ su $Y$, condizionando rispetto a tutti gli altri $X_j$.

Aggiungendo una variabile indipendente al modello, si possono modificare i valori degli altri coefficienti e i loro p-value e si riduce l'incertezza $\epsilon$. Questo avviene perchè con meno variabili il modello ha una porzione di varianza maggiore da attribuire all'errore stocastico $\epsilon$, che viene ridotta nel caso in cui vengono aggiunte altre variabili indipendenti.

### Esempio di output di una regressione lineare multipla

Sia $Y=mpg$, $X_1=horsepower$ e $X_2=weight$, un possibile output di una regressione lineare potrebbe essere:
<table>
    <tr>
        <th></th>
        <th>COEFFICIENT</th>
        <th>STD ERROR</th>
        <th>t</th>
        <th>P-value</th>
        <th>CONFIDENCE INTERVAL</th>
    </tr>
    <tr>
        <td>&beta;<sub>0</sub></td>
        <td>39.94</td>
        <td>0.717</td>
        <td>55.66</td>
        <td>0</td>
        <td>[38.53, 41.35]</td>
    </tr>
    <tr>
        <td>&beta;<sub>1</sub></td>
        <td>-0.1578</td>
        <td>0.006</td>
        <td>-24.49</td>
        <td>0</td>
        <td>[-0.17, -0.15]</td>
    </tr>
    <tr>
        <td>&beta;<sub>2</sub></td>
        <td>-0.0025</td>
        <td>0.0003</td>
        <td>-8.21</td>
        <td>0</td>
        <td>[-0.003, -0.002]</td>
    </tr>
</table>

___
### F-test 

Viene utilizzato per verificare che ci sia correlazione tra le variabili indipendenti e la variabile dipendente prima di fittare il reggressore.

$$H_0: \text{Non c'è una correlazione significativa tra gli } X_i \text{ ed } Y \Leftrightarrow \forall i \quad B_i=0$$
$$H_1: \text{C'è una correlazione significativa tra gli } X_i \text{ ed } Y \Leftrightarrow \exists i \quad B_i \neq 0$$

dove:

$$F = \frac{(TSS - RSS) / n}{RSS / (m - n - 1)}$$

con $n$ numero di variabili indipendenti e $m$ numero di osservazioni.

Se $p_{-value} < \alpha$ allora si rigetta l'ipotesi nulla, ovvero si afferma che almeno una variabile indipendente è significativamente correlata alla variabile dipendente.

___

### Backward Elimination (Variable Selection)

L'aggiunta di variabili al modello aumenta sempre (o lascia invariato) il valore di $ R^2 $, anche quando le variabili aggiunte sono ridondanti o non correlate con la variabile dipendente $ Y $. 

Questo fenomeno si verifica perché $ R^2 $ misura la proporzione di varianza spiegata dal modello: ogni variabile aggiuntiva porta un miglioramento, seppur minimo, o non peggiora mai il fit complessivo.

Tuttavia, un aumento di $ R^2 $ non implica necessariamente che il modello sia migliorato in termini di interpretabilità o di capacità predittiva. Infatti:

1. **Selezionare un Livello di Significatività**:
   - Prima di iniziare, stabilire un livello di significatività (es. $ \alpha = 0.05 $) per decidere se una variabile deve essere rimossa dal modello.

2. **Fittare il Modello Iniziale**:
   - Iniziasi considerano tutte le variabili indipendenti disponibili per la regressione. 

3. **Valutare i P-Value delle Variabili**:
   - Esaminare i p-value delle variabili nel modello ottenuto, concentrandosi sulla variabile con il p-value più alto. Un p-value elevato suggerisce che la variabile potrebbe non contribuire in modo significativo al modello.

4. **Rimuovere la Variabile Non Significativa**:
   - Se il p-value della variabile con il valore più alto è maggiore del livello di significatività, procedere alla sua rimozione dal modello.

5. **Rifittare il Modello**:
   - Ripetere il fit del modello utilizzando le variabili rimanenti, escludendo quella appena rimossa. Questo modello ora rappresenta una versione più semplice e potenzialmente più efficace del modello originale.

6. **Ripetere il Processo**:
   - Tornare al passaggio 3 e ripetere il processo fino a quando tutte le variabili rimanenti nel modello risultano significative secondo il livello di significatività scelto.

### Nota Importante 
I p-value per ogni coefficiente si ottengono impostando un test di significatività dei coefficienti con la seguente statistica: $$t = \frac{\hat{\beta}_1 - 0}{SE(\hat{\beta}_1)}$$

### Adjusted $R^2$

A differenza di $ R^2 $, che aumenta sempre quando aggiungiamo variabili, $ R^2 $ adjusted considera sia la complessità del modello sia la dimensione del campione per capire se una nuova variabile contribuisce realmente alla spiegazione della variabilità di $ Y $ o se rende il modello solo più complesso senza migliorarlo.

$$\bar{R}^2 = 1 - \frac{m-1}{m-n-1}(1-R^2)$$

con $m$ numero di osservazioni e $n$ numero di variabili indipendenti.

___

## Reressione Polinomiale

Un modello di regressione polinomiale è un modello di regressione lineare in cui la relazione tra la variabile dipendente $Y$ e la variabile indipendente $X$ è modellata come un polinomio di grado $n$. 

$$Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \ldots + \beta_n X^n + \epsilon$$

La regressione polinomiale è utile quando:
- La relazione tra le variabili non è lineare ma può essere approssimata da una curva.
- Il modello lineare semplice risulta inadatto e presenta errori sistematici (per esempio, con una chiara curvatura nei dati).

**OSSERVAZIONI**:

1. La regressione polinomiale è ancora un modello di regressione lineare, poiché i coefficienti $\beta_0, \beta_1, \ldots, \beta_n$ sono ancora stimati utilizzando il metodo dei minimi quadrati.
2. La regressione polinomiale rende il significato dei coefficienti meno intuitivo da un punto di vista statistico poiché ora rappresentano l'effetto di un incremento di $X$ al quadrato, al cubo, ecc.

### Q-Q Plot dei residui 

I residui gaussiani indicano che le deviazioni tra i valori osservati e quelli previsti dal modello non seguono un pattern specifico. In altre parole, gli errori sono casuali e non sistematici. Questo significa che non ci sono fattori non catturati dal modello che influenzano i dati in modo prevedibile.
Per verificare che i residui (gli errori) siano distribuiti normalmente, si può utilizzare un Q-Q plot. 

In particolare si graficano i valori reali di $Y$ rispetto ai residui stimati dal modello. Se i residui sono distribuiti normalmente, i punti nel Q-Q plot dovrebbero seguire una linea retta.

#### Costruzione di un Q-Q Plot:

1. **Calcolo dei residui**: Si calcolano i residui, che rappresentano la differenza tra i valori osservati e quelli previsti dal modello.

2. **Ordinamento dei residui**: I residui vengono ordinati in ordine crescente per poter calcolare i quantili empirici.

3. **Calcolo dei quantili teorici**: Per ogni quantile empirico dei residui, si calcola il corrispondente quantile teorico della distribuzione normale (assumendo una media di 0 e una deviazione standard di 1, se il modello è standardizzato).

4. **Creazione del grafico**: Si tracciano i quantili teorici della distribuzione normale sull'asse X e i quantili empirici dei residui sull'asse Y.

#### Interpretazione del Q-Q Plot:
- **Deviazioni dalla linearità**: Se i punti si discostano significativamente dalla linea, ciò suggerisce che i residui potrebbero non seguire una distribuzione normale:
  - **Code più spesse**: Se i punti ai margini (code) del grafico si discostano dalla linea retta, potrebbe indicare la presenza di una distribuzione con code più spesse rispetto alla normale (ad esempio, una distribuzione leptocurtica).
  - **Asimmetrie**: Una deviazione dalla linearità solo da un lato (es. solo nella parte superiore o inferiore) può indicare una distribuzione asimmetrica dei residui.
- **Normalità**: Se i punti seguono una linea retta, allora i residui sono distribuiti normalmente e il modello di regressione è appropriato.
___ 
### Metodo dei minimi quadrati per la stima di $\beta$

Il **metodo dei minimi quadrati** è un metodo per stimare i coefficienti di regressione $\beta$ in un modello di regressione lineare. L'obiettivo è trovare i valori di $\beta$ che minimizzano la somma dei quadrati degli errori, definita come:

$$
\beta = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i)^2
$$

Per generalizzare questo approccio in forma matriciale, definiamo:

- $\mathbf{X}$ come la matrice delle variabili indipendenti (feature),
- $\mathbf{y}$ come il vettore dei valori osservati della variabile dipendente,
- $\mathbf{\beta}$ come il vettore dei coefficienti di regressione che vogliamo stimare.

$$
RSS = \sum_{i=1}^{m} \left(y_i - \beta_0 - \sum_{j=1}^{n} \beta_j x_{ij}\right)^2 = \sum_{i=1}^{m} e_i^2 = \mathbf{e}^T \mathbf{e}
$$

La funzione obiettivo può essere riscritta come:

$$
\text{RSS} = (\mathbf{y} - \mathbf{X} \mathbf{\beta})^T (\mathbf{y} - \mathbf{X} \mathbf{\beta})
$$

Per minimizzare la RSS, calcoliamo la derivata rispetto a $\mathbf{\beta}$ e la poniamo uguale a zero:

$$
\frac{\partial}{\partial \mathbf{\beta}} \text{RSS} = -2 \mathbf{X}^T (\mathbf{y} - \mathbf{X} \mathbf{\beta}) = 0
$$

Risolvendo per $\mathbf{\beta}$, otteniamo:

$$
\mathbf{\beta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}
$$

In questo passaggio appare la **trasposta di $\mathbf{X}$**: essa è necessaria per trasformare l'equazione in modo che possiamo risolvere per $\mathbf{\beta}$ in forma matriciale.
___

### Multicollinearità

La **multicollinearità** si verifica quando due o più variabili indipendenti (o "feature") in un modello di regressione sono fortemente correlate tra loro. 

Se consideriamo una matrice $\mathbf{X}$ delle variabili indipendenti che contiene due feature molto simili, il prodotto $\mathbf{X}^T \mathbf{X}$ (necessario per calcolare $\mathbf{\beta}$ nel metodo dei minimi quadrati) può risultare **non invertibile** o quasi. Questo rende il calcolo di $\mathbf{\beta}$ instabile, perché il modello non riesce a separare l'influenza di ciascuna variabile.

Se $\mathbf{X}^T \mathbf{X}$ è singolare o quasi singolare, il modello diventa meno affidabile e le stime dei coefficienti possono risultare poco interpretabili o sensibili a piccole variazioni nei dati.

### Ridge Regression

La **Ridge Regression** è una tecnica utilizzata per affrontare il problema della multicollinearità. Invece di eliminare variabili indipendenti correlate, Ridge Regression aggiunge un termine di penalizzazione alla funzione di costo per ridurre la variabilità dei coefficienti.

La funzione di costo modificata per Ridge Regression è:

$$
\text{RSS}_{ridge} = \sum_{i=1}^{m} \left( y_i - \beta_0 - \sum_{j=1}^{n} \beta_j x_{ij} \right)^2 + \lambda \sum_{j=1}^{n} \beta_j^2
$$

dove $\lambda$ è un parametro che controlla la quantità di penalizzazione. Se $\lambda$ è grande, Ridge Regression riduce i coefficienti $\beta_j$ verso lo zero, limitando così l’effetto della multicollinearità. Questo metodo migliora la stabilità del modello e riduce il rischio di overfitting.

#### Interpretazione dei coefficienti in Ridge Regression

I coefficienti stimati in Ridge Regression tendono ad avere **valori più piccoli** rispetto a quelli di una regressione lineare classica. Questo è dovuto al **termine di regolarizzazione** che spinge i coefficienti verso valori più bassi. Di conseguenza, i parametri della Ridge Regression non possono essere interpretati statisticamente nello stesso modo dei coefficienti di una regressione lineare standard; 

Possiamo invece interpretare questi coefficienti come un **indicatore dell'importanza relativa** delle variabili per la predizione. Un valore più grande indica che la variabile ha un'influenza maggiore nella predizione, mentre un valore più piccolo implica un'influenza ridotta, pur senza azzerarsi completamente.
___

### Lasso Regression

La **Lasso Regression** è un'altra tecnica di regressione che, come Ridge Regression, utilizza una penalizzazione per migliorare la stabilità del modello. Tuttavia, Lasso aggiunge una penalizzazione **L1** invece della penalizzazione **L2** di Ridge. La funzione di costo per Lasso Regression è:

$$
\text{RSS}_{lasso} = \sum_{i=1}^{m} \left( y_i - \beta_0 - \sum_{j=1}^{n} \beta_j x_{ij} \right)^2 + \lambda \sum_{j=1}^{n} |\beta_j|
$$

A differenza di Ridge Regression, la penalizzazione L1 di Lasso porta molti coefficienti $\beta_j$ esattamente a zero quando $\lambda$ è sufficientemente grande. Questo rende Lasso particolarmente utile per la **selezione delle variabili**, poiché elimina automaticamente dal modello le variabili meno rilevanti.

#### Interpretazione dei coefficienti in Lasso Regression

Come si può osservare, il modello con Lasso Regression effettua delle "scelte nette" su quali variabili mantenere e quali impostare a zero, realizzando così una selezione esplicita delle variabili. Questo processo di selezione identifica automaticamente le variabili meno influenti per la predizione, riducendo la complessità del modello e migliorando l'interpretabilità.

### Variable selection

- Lasso non solo riduce i coefficienti come Ridge, ma azzera esplicitamente quelli meno rilevanti, realizzando una vera **selezione delle variabili**.
- Dopo l'applicazione di Lasso, possiamo costruire un modello lineare tradizionale e interpretabile, utilizzando solo le variabili selezionate e i dati originali, senza la necessità di ulteriori trasformazioni.

___

### Regressione Logistica

La **Regressione Logistica** è un modello di regressione utilizzato per la classificazione binaria. A differenza della regressione lineare, che prevede una variabile continua, la regressione logistica prevede una variabile binaria (0 o 1).

### Funzione Logistica

Vorremmo predirre la probabilità di appartenenza ad una delle due classi (solitamente la classe 1) in base ai valori delle variabili indipendenti. Abbiamo quindi bisogno di applicare una funzione al regressore lineare che abbia le seguenti caratteristiche:

- **Output compreso tra 0 e 1**: La funzione deve produrre un output compreso tra 0 e 1, poiché vogliamo interpretare il risultato come una probabilità.

- **Monotonicità**: La funzione deve essere monotona rispetto al regressore lineare, in modo che un incremento delle variabili indipendenti porti a un aumento o diminuzione sistematica della probabilità prevista, senza oscillazioni. Questo permette una relazione interpretabile tra le variabili indipendenti e la probabilità.

- **Saturazione**: La funzione dovrebbe tendere a 0 per valori molto bassi del regressore lineare e a 1 per valori molto alti. Questo rispetta l'idea che per valori estremi delle variabili indipendenti, la probabilità di appartenere a una delle due classi diventi quasi certa.

La più semplice funzione che soddisfa queste caratteristiche è la **funzione logistica**:

$$f(x) = \sigma(x) =\frac{1}{1 + e^{-x}}$$

### Regressore Logistico

Il modello di regressione logistica è definito come:

$$P(Y=1|X) = \sigma(\beta^T \cdot X) = \frac{1}{1 + e^{-(\beta^T \cdot X)}}$$

dove:
- $P(Y=1|X)$ è la probabilità che la variabile dipendente $Y$ sia uguale a 1, dato il vettore delle variabili indipendenti $X$.
- $\sigma$ è la funzione logistica, che trasforma il prodotto scalare $\beta^T \cdot X$ in un valore compreso tra 0 e 1.
- $\beta$ è il vettore dei coefficienti di regressione.
- $X$ è il vettore delle variabili indipendenti.

Si può riscrivere il modello di regressione logistica in funzione del **logit**:

$$log\left(\frac{P(Y=1|X)}{1 - P(Y=1|X)}\right) =  \beta^T \cdot X$$

da cui

$$\frac{P(Y=1|X)}{1 - P(Y=1|X)} = e^{\beta^T \cdot X}$$

Sebbene la funzione logistica (o sigmoide) non sia lineare, il modello di regressione logistica è un **classificatore lineare**: la decision boundary è determinata dalla combinazione lineare delle variabili.

**Interpretazione statistica dei coefficienti**:

- **$e^{\beta_0}$** rappresenta l' odds di $Y=1$ , quando tutte le variabili indipendenti $x_i$ sono uguali a zero.

- **$e^{\beta_i}$** rappresenta il fattore moltiplicativo dell' odds di $Y=1$ associato a un incremento di una unità nella variabile $x_i$, mantenendo costanti tutte le altre variabili $x_j$ ($j \neq i$). In altre parole:
    - Se $e^{\beta_i} = 1.05$, un incremento unitario in $x_i$ aumenta gli odds di $Y = 1$ del 5%.
    - Se $e^{\beta_i} = 0.95$, un incremento unitario in $x_i$ diminuisce gli odds di $Y = 1$ del 5%.

**Interpretazione geometrica dei coefficienti**:

Geometricamente, i coefficienti $\beta_0$ e $\beta_i$ insieme definiscono la posizione e l'orientamento della **decision boundary**, separando le classi in base ai valori delle variabili. 

La decision boundary si ottiene quando:

$$\beta^T \cdot X = 0$$

Questa equazione rappresenta una linea in due dimensioni, un piano in tre dimensioni, e in generale un iperpiano, separando le classi nel modo più semplice possibile.

### Negative Log Likelihood (NLL)

La funzione di costo tiene conto del concetto di verosimiglianza (**likelihood**), ovvero la probabilità di osservare i dati sotto al modello stimato dai parametri $\beta$.

$$L(\beta)=\prod_{i=1}^{m} P(y_i | x_i, \beta)$$

Poichè risulta più comodo lavorare con un problema di minimo invece che di massimo, si considera di minimizzare la **negative likelihood** data da :

$$-L(\beta)=-\prod_{i=1}^{m} P(y_i | x_i, \beta)$$

Poiché il calcolo di un prodotto di probabilità può essere numericamente instabile (rischio di **underflow**), è preferibile utilizzare il **logaritmo della negative likelihood**, che converte il prodotto probabilià in una somma di logaritmi:

$$
- \log(L(\beta)) = -\sum_{i=1}^{m} \log(P(y_i \mid x_i, \beta)) = -\sum_{i=1}^{m} \left[ y_i \log \hat{y_i} + (1-y_i) \log (1 - \hat{y_i})\right] = -\sum_{i=1}^{m} \left[ y_i \log \left( \frac{1}{1+e^{-\beta^T X_i}} \right) + (1-y_i) \log \left( 1 - \frac{1}{1+e^{-\beta^T X_i}} \right)\right]
$$

La Negative Log Likelihood (NLL) è una misura basata sul principio della massimizzazione della verosimiglianza. In altre parole, vogliamo che il modello attribuisca una probabilità elevata agli esiti osservati, così da rappresentare al meglio i dati forniti. Minimizzare la NLL equivale a massimizzare la verosimiglianza del modello, poiché stiamo cercando i valori di $ \beta $ che rendano massima la probabilità che il modello rappresenti correttamente i dati osservati.

### Soluzione ottima

A differenza della regressione lineare, dove la funzione di costo è basata su una somma dei quadrati degli errori (metodo dei minimi quadrati), la funzione di costo della regressione logistica è **non lineare** rispetto ai parametri $ \beta $. Questo significa che non possiamo risolvere il problema con una formula chiusa (cioè un’espressione analitica come nella regressione lineare). Di conseguenza, dobbiamo utilizzare metodi iterativi come il **gradient descent** per stimare i parametri $ \beta $.
____
## Regressione Logistica Multinomiale

La **Regressione Logistica Multinomiale** è una generalizzazione della regressione logistica per il caso di più di due classi.

### Intuizione (One-vs-Rest)

Per semplificare i calcoli, si sceglie una delle $K$ classi come baseline class, ovvero si fissa una classe di riferimento.
Nella regressione logistica binaria, modelliamo il logaritmo degli odds come una combinazione lineare delle variabili indipendenti. 
Nella regressione logistica multinomiale, invece, modelliamo il logaritmo del rapporto delle probabilità di appartenenza ciascuna classe ($Y = k$) e la classe di riferimento ($Y=1$) con una combinazione lineare delle variabili.

Il modello di regressione logistica multinomiale per la classe $k$ rispetto alla classe di riferimento è:

$$P(Y=k|X) = \frac{e^{\beta_k^T \cdot X}}{1 + \sum_{j=2}^{K} e^{\beta_j^T \cdot X}}$$

Si ha quindi un modello di regressione logistica per ogni classe, ovvero per $K$ classi si hanno $K-1$ modelli di regressione logistica, tutti che stimano $n$ coefficienti. Si hanno quindi $K-1 \times (n+1)$ coefficienti da stimare.

Scrivendo in funzione del logit si ha:

$$log(\frac{P(Y=k|X)}{P(Y=1|X)}) = \beta_k^T \cdot X$$

da cui si ottiene:

$$\frac{P(Y=k|X)}{P(Y=1|X)} = e^{\beta_k^T \cdot X}$$

### Interpretazione statistica dei coefficienti

- L'intercetta mi dice che se tutte le variabili indipendenti sono uguali a zero, la probabilità di appartenenza alla classe di riferimento rispetto ad appartenere alla classe base (odds) è pari a $e^{\beta_0}$.

- Il coefficiente $\beta_i$ mi dice come cambia in maniera moltiplicativa la probabilità di appartenenza alla classe di riferimento per un incremento di una unità della variabile $X_i$, mantenendo costanti tutte le altre variabili. Per esempio, se $e^{\beta_i} = 1.05$, un incremento unitario in $X_i$ aumenta gli odds di appartenenza alla classe di riferimento del 5%.

___
## Analisi Causale

- **Treatment**: variabile che rappresenta l'intervento o trattamento che si vuole valutare.

  All'interno del treatment si distinguono due categorie:

  - **Treatment group (treated)**: gruppo di osservazioni che ricevono il trattamento.

  - **Control group (untreated)**: gruppo di osservazioni che non ricevono il trattamento.

- **Outcome**: variabile che rappresenta l'effetto dell'intervento o trattamento.

- **Potential Outcome (Counterfactual)**: rappresenta ciò che sarebbe successo in assenza di trattamento. Si nota che non possiamo osservare contemporaneamente il trattamento e il controllo, quindi non possiamo osservare direttamente i potential outcome.

- **ATE (Average Treatment Effect)**: rappresenta la differenza media tra l'outcome nel treatment group e l'outcome nel control group. L'ATE ci dice come cambierebbe, in media, l'outcome per l'intera popolazione se tutti ricevessero il trattamento rispetto a nessuno.

$$ATE=E[Y(1)−Y(0)]$$

- **ATT (Average Treatment Effect on the Treated)**: rappresenta la differenza media tra l'outcome nel treatment group e l'outcome nel control group tra le osservazioni che hanno effettivamente ricevuto il trattamento. L'ATT ci dice qual è l'effetto del trattamento limitato al gruppo che effettivamente lo ha ricevuto.

$$ATT=E[Y(1)−Y(0)∣T=1]$$

- **Bias**: Il bias misura la differenza tra il risultato medio atteso per i trattati se non fossero stati trattati $E[Y(0)∣T=1]$ e il risultato medio atteso per i non trattati $E[Y(0)∣T=0]$. 

  Quando calcoliamo il bias, vogliamo capire se i trattati e i non trattati erano simili prima che il trattamento fosse applicato. In altre parole, vogliamo sapere quale sarebbe stato l’esito medio per i trattati se non fossero stati trattati.

$$BIAS=E[Y(0)∣T=1]−E[Y(0)∣T=0]$$

Quindi il Bias è nullo quando i gruppi trattati e di controllo sono comparabili per tutto tranne che per il trattamento.

  Si ha che 

$$E[Y(1)|T=1]-E[Y(0)∣T=0]=ATT+Bias$$

____
## Esempio di Calcolo di ATE, ATT e Bias

|    | Treatment \( T=1 \) | Control \( T=0 \) |
|----|----------------------|-------------------|
| Alfio  | 10                  | <span style="color:red">8</span>                 |
| Simone  | 10                   | <span style="color:red">5</span>                 |
| Lele  | <span style="color:red">11</span>                  | 5                  |
|    | Y(1)                  | Y(0)                 |

**Notazione** : $\textcolor{red}{n}$ evidenziato in rosso denota un potential oucome (counterfactual).

- **ATE (Average Treatment Effect)**:
  $$
  ATE = E[Y(1) - Y(0)] = \frac{(10 - \textcolor{red}{8}) + (10 - \textcolor{red}{5}) + (\textcolor{red}{11} - 5)}{3} = 3.67
  $$

- **ATT (Average Treatment Effect on the Treated)**:
  $$
  ATT = E[Y(1) - Y(0) \mid T=1] = \frac{(10 - \textcolor{red}{8}) + (10 - \textcolor{red}{5})}{2} = 3.5
  $$

- **Bias**:
  $$
  \text{Bias} = E[Y(0) \mid T=1] - E[Y(0) \mid T=0] = \frac{\textcolor{red}{8} + \textcolor{red}{5}}{2} - 5 = 1.5
  $$
____

  La correlazione è di causa-effetto quando i gruppi treated e di controllo sono comparabili per tutto tranne che per il trattamento. Il metodo più robusto per rimuovere questo bias è tramite esperimenti randomizzati.

- **RCT (Randomized Controlled Trial)**: è uno studio sperimentale in cui i partecipanti vengono assegnati casualmente a un gruppo di trattamento o a un gruppo di controllo.

- **Condizionare per $X$**: significa condizionare rispetto a una variabile $X$, ovvero considerare i dati solo per un sottoinsieme di osservazioni in cui $X$ assume un valore specifico.

$$Y(0) \perp Y(1)|X$$

La scritta sopra mi dice che, fissato il valore per $X$, conoscere $Y(0)$ non mi dice nulla su $Y(1)$. Condizionando rispetto ad $X$ si eliminano i bias dovuti a differenze sistematiche tra i gruppi trattati e di controllo. 

Il condizionamento su qualsiasi variabile non è un buon modo per eliminare i bias. Se condizioniamo la variabile “sbagliata”, potremmo introdurre un bias che non c'era in origine e stimare l'assenza di un effetto causale anche nei casi in cui l'effetto causale è presente.

## Causal Graph

Un **causal graph** è un grafo diretto che rappresenta le relazioni causali tra le variabili di un sistema. Le frecce nel grafo indicano la direzione della causalità, ovvero come una variabile influenza un'altra.

### Chain, Fork e Collider

- **Chain**: una struttura a catena si verifica quando una variabile $ A $ influenza una variabile $ B $, che a sua volta influenza una variabile $ C $. In questo caso, $ B $ è una variabile mediatrice.

  - La dipendenza causale tra $ A $ e $ C $ viene bloccata se condizioniamo sulla variabile $ B $ (variabile mediatrice), eliminando l’effetto di $ A $ su $ C $.

  $$ A \rightarrow B \rightarrow C $$

- **Fork**: una struttura a forca si verifica quando una variabile comune $ C $ influenza due variabili separate $ A $ e $ B $. In questo caso, $ C $ è una causa comune e introduce una dipendenza tra $ A $ e $ B $.

  - La dipendenza tra $ A $ e $ B $ viene bloccata se condizioniamo sulla variabile $ C $, eliminando l’effetto della causa comune.

  $$ A \leftarrow C \rightarrow B $$

- **Collider**: una struttura a collider si verifica quando due variabili $ A $ e $ B $ influenzano una terza variabile $ C $. In questo caso, $ C $ è chiamata collider e blocca la dipendenza tra $ A $ e $ B $.

  - La dipendenza causale tra $ A $ e $ B $ viene sbloccata (cioè si crea una correlazione) se condizioniamo sulla variabile $ C $.

  $$ A \rightarrow C \leftarrow B $$

### Regola di Blocco
Ricordiamo inoltre che abbiamo detto che un percorso tra $A$ e $B$ è bloccato se:

- contiene un non-collider su cui è stato condizionato;
- contiene un collider che non è stato condizionato e non ha discendenti condizionati.

### Bias

**Confounding Bias**: Il confounding bias si verifica quando non si controlla una causa comune (confounder) che influenza sia il trattamento $T$ che l’outcome $Y$. Questa mancanza di controllo porta a una correlazione spuria tra il trattamento e l’outcome. Per evitare questo tipo di bias, è necessario condizionare sul confounder (la causa comune). In questo modo, possiamo isolare meglio l’effetto del trattamento sull’outcome, eliminando l’influenza della variabile confondente.

- **Confounder** : variabile che influenza sia il trattamento che l'outcome. La presenza di confounders può portare a una sovrastima o sottostima dell'effetto del trattamento sull'outcome. Se ci sono confounders la correlazione indica probabilmente un rapporto di causa-effetto.

**Selection Bias**: Il selection bias si presenta in due forme principali:

- Selection Bias - **Common Effect**: Questo tipo di bias si verifica quando si controlla un effetto comune di due variabili, una delle quali è il trattamento $T$ e l'altra è una variabile aggiuntiva correlata all’outcome $Y$. Quando controlliamo per un effetto comune, introduciamo artificialmente una relazione tra trattamento e outcome. In questo caso, non dovremmo controllare l'effetto comune per evitare distorsioni.

- Selection Bias - **Mediator**: Questo tipo di bias si verifica quando si controlla un mediatore tra trattamento $T$ e outcome $Y$. Un mediatore è una variabile che si trova sulla strada causale tra il trattamento e l'outcome. Controllare un mediatore interrompe il percorso causale tra $T$ e $Y$, introducendo bias. In questo caso, non dovremmo controllare sul mediatore.
### Regressione Lineare in analisi Causale

- **Problema**: la regressione lineare non è adatta per stimare l'effetto causale di un trattamento o intervento.
Questo perchè la regressione lineare non tiene conto del **confounding bias**, ovvero la presenza di variabili nascoste che influenzano sia il trattamento che l'outcome.

___

## Dati come punti N-dimensionali

### Space representation

- **Feature Space**: spazio delle variabili indipendenti, rappresentato da un vettore $x \in \mathbb{R}^d$. Ogni variabile corrisponde a una dimensione nello spazio.

### Funzione di rappresentazione (feauture representation)

$$f: \mathbb{R}^d \rightarrow \mathbb{R}^m$$

- **Input Space**: spazio delle variabili indipendenti, rappresentato da un vettore $x \in \mathbb{R}^d$.
- **Output Space**: spazio delle variabili dipendenti, rappresentato da un vettore $y \in \mathbb{R}^m$.

### Norme (P-norm)

$$\|\mathbf{x}\|_p = \left( \sum_{i=1}^{d} |x_i|^p \right)^{\frac{1}{p}}$$

- **Norma L1**: $\|\mathbf{x}\|_1 = \sum_{i=1}^{d} |x_i|$

- **Norma L2**: $\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^{d} x_i^2}$

- **Norma $L2^2$**: $\|\mathbf{x}\|_{2}^2 = \sum_{i=1}^{d} x_i^2$

- **Norma L$\infty$**: $\|\mathbf{x}\|_{\infty} = \max_{i} |x_i|$

### Metriche di distanza

Dato uno spazio $S$ si ha :

$$m : S \times S \rightarrow \mathbb{R}$$

Una metrica gode delle seguenti proprietà:

1. La distanza di un punto da sé stesso è zero: $ m(\mathbf{x}, \mathbf{x}) = 0 $;

2. La distanza tra due punti distinti è sempre positiva (positività) se $ \mathbf{x} \neq \mathbf{y} $:
   $ m(\mathbf{x}, \mathbf{y}) \geq 0, \, \forall \mathbf{x}, \mathbf{y} \in S, \, \mathbf{x} \neq \mathbf{y} $;

3. La distanza tra $ x $ e $ y $ è la stessa della distanza tra $ y $ e $ x $ (simmetria):
   $ m(\mathbf{x}, \mathbf{y}) = m(\mathbf{y}, \mathbf{x}) $;

4. Disuguaglianza triangolare:
   $ m(\mathbf{x}, \mathbf{y}) \leq m(\mathbf{x}, \mathbf{z}) + m(\mathbf{z}, \mathbf{y}), \, \forall \mathbf{x}, \mathbf{y}, \mathbf{z} \in S $.

### Metriche LP

$$L_p(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\|_p = \left( \sum_{i=1}^{d} |x_i - y_i|^p \right)^{\frac{1}{p}}$$

- **Distanza L1**: $L_1(\mathbf{x}, \mathbf{y}) = \sum_{i=1}^{d} |x_i - y_i|$

- **Distanza L2**: $L_2(\mathbf{x}, \mathbf{y}) = \sqrt{\sum_{i=1}^{d} (x_i - y_i)^2}$

- **Distanza L$\infty$**: $L_{\infty}(\mathbf{x}, \mathbf{y}) = \max_{i} |x_i - y_i|$

### Cosine Similarity

La **Cosine Similarity** è una misura di similarità tra due vettori nello spazio. La similarità coseno è definita come il coseno dell'angolo tra i due vettori.

$$\text{Cosine Similarity} = \cos(\theta) = \frac{\mathbf{x} \cdot \mathbf{y}}{\|\mathbf{x}\|_2 \|\mathbf{y}\|_2}$$

**Interpretazione**:
- Se i due vettori sono simili, l'angolo tra di loro è piccolo e la similarità coseno è vicina a 1.
- Se i due vettori sono ortogonali, l'angolo tra di loro è di 90 gradi e la similarità coseno è 0.
- Se i due vettori sono opposti, l'angolo tra di loro è di 180 gradi e la similarità coseno è -1.

### Cosine Distance

La **Cosine Distance** è una misura di dissimilarità tra due vettori nello spazio. La distanza coseno è definita come l'angolo tra i due vettori.

$$\text{Cosine Distance} = 1 - \cos(\theta) = 1 - \frac{\mathbf{x} \cdot \mathbf{y}}{\|\mathbf{x}\|_2 \|\mathbf{y}\|_2}$$

**Interpretazione**:
- Se i due vettori sono simili, l'angolo tra di loro è piccolo e la distanza coseno è vicina a 0.
- Se i due vettori sono ortogonali, l'angolo tra di loro è di 90 gradi e la distanza coseno è 1.
- Se i due vettori sono opposti, l'angolo tra di loro è di 180 gradi e la distanza coseno è 2.

____

## Clustering

Il **clustering** è una tecnica di unsupervised learning che consiste nel raggruppare insiemi di dati simili in cluster. L'obiettivo è trovare una struttura nascosta nei dati senza etichette, suddividendoli in gruppi omogenei.

Si assume di avere un insieme di dati $X = \{x^{(i)}\}$

$$\mathbf{X} = \left\{ \mathbf{x}^{(i)} \right\}_{i=1}^N, \quad \mathbf{x}^{(i)} \in \mathbb{R}^n$$

L'obiettivo del clustering è trovare una partizione dei dati in cluster omogenei, in modo che i dati all'interno di ciascun cluster siano simili tra loro e diversi da quelli in altri cluster.

$$S = \{ S_1, S_2, \dots, S_K \}$$

dove $S_j$ è il $j$-esimo cluster e $K$ è il numero di cluster.

____
### K-Means Clustering

Il **K-Means** è un algoritmo di clustering che assegna i punti ai cluster in modo che la somma delle distanze quadrate tra i punti e il centroide del cluster sia minima.

#### Algoritmo K-Means:

1. **Inizializzazione**: Scegliere casualmente $K$ centroidi iniziali.
2. **Assegnazione dei punti ai cluster**: Assegnare ciascun punto al cluster con il centroide più vicino.
3. **Aggiornamento dei centroidi**: Calcolare i nuovi centroidi come la media dei punti assegnati a ciascun cluster.
4. **Ripetizione**: Ripetere i passaggi 2 e 3 fino a convergenza.
