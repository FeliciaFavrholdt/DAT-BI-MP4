

## Which machine learning methods did you choose to apply in the application and why?

Vi valgte forskellige machine learning-metoder afhængigt af opgavetypen. Til regressionsopgaven, hvor vi skulle forudsige månedlig indkomst, anvendte vi lineær regression, da den er simpel, fortolkelig og velegnet til kontinuerlige målvariable. Den gør det muligt at forstå, hvordan fx erfaring, uddannelse og jobniveau påvirker lønnen. Til klassifikationsopgaven, hvor vi skulle forudsige, om en medarbejder forlader jobbet (attrition), anvendte vi Random Forest, da metoden er god til at håndtere både kategoriske og numeriske variable, samtidig med at den kan modellere komplekse ikke-lineære sammenhænge. Logistisk regression blev anvendt som baseline-model på grund af dens enkle struktur og fortolkelighed. Til clustering-opgaven anvendte vi K-Means, da det er en effektiv metode til at gruppere medarbejdere i segmenter baseret på ligheder i deres karakteristika. Antallet af klynger blev valgt ud fra den højeste silhouette score, som angiver, hvor godt adskilt og sammenhængende klyngerne er.

## How accurate is your solution of prediction? Explain the meaning of the quality measures.

Klassifikationsmodellen til forudsigelse af medarbejder-attrition opnåede en præcision (accuracy) på omkring 85-90% på testdatasættet. Vi brugte flere kvalitetsmål for at vurdere modellens præstation: accuracy viser andelen af korrekte forudsigelser, precision måler hvor stor en andel af de forudsagte jobskifter der faktisk er korrekte, recall viser hvor stor en andel af de faktiske jobskifter modellen fanger, og F1-score balancerer precision og recall i ét samlet mål, hvilket er særligt nyttigt ved ubalancerede datasæt. Til regressionsmodellen, som forudsagde månedlig indkomst, anvendte vi R² og RMSE som mål for kvalitet. R² (forklaringsgraden) viser hvor stor en andel af variationen i løn modellen kan forklare, og RMSE (root mean squared error) angiver den gennemsnitlige afvigelse mellem forudsagte og faktiske værdier jo lavere RMSE, desto mere præcise forudsigelser.

## Which are the most decisive factors for quitting a job? Why do people quit their job?

De mest afgørende faktorer for at forlade jobbet var lav jobtilfredshed, begrænsede karrieremuligheder, dårligt arbejdsmiljø, lav løn i forhold til markedet og lange pendlingstider. Mange medarbejdere vælger at forlade virksomheden, når de oplever utilfredsstillende arbejdsforhold, manglende balance mellem arbejde og privatliv, og når de ikke ser mulighed for faglig eller personlig udvikling. Vores model viste, at variable som jobtilfredshed, distance til arbejde, arbejdspres og overtime ofte hænger sammen med attrition.

## What could be done for further improvement of the accuracy of the models?

For at forbedre modellernes nøjagtighed kunne vi indsamle mere detaljerede og opdaterede data, herunder kvalitative oplysninger som feedback fra medarbejdere eller resultater fra tilfredshedsundersøgelser. Vi kunne også inkludere flere relevante features, som fx ledelsesstil, teamdynamik og det psykiske arbejdsmiljø. Desuden kunne vi eksperimentere med mere avancerede modeller som neurale netværk, især hvis datasættet udvides. I klassifikationsopgaven kunne vi anvende teknikker som SMOTE til at håndtere ubalancerede klasser og optimere hyperparametre gennem fx grid search eller bayesiansk optimering for at opnå bedre modelperformance.

## Which work positions and departments are in higher risk of losing employees?

Vores analyse viste, at medarbejdere i salgs- og kundeserviceafdelinger oftere forlader virksomheden, sandsynligvis på grund af høje krav, stress og lav jobtilfredshed. Derudover var roller inden for teknisk support og visse administrative funktioner også præget af højere udskiftning, ofte fordi disse stillinger er rutineprægede, lavere lønnede og med færre udviklingsmuligheder. Positioner med meget overarbejde og lav intern mobilitet så også ud til at have højere risiko for attrition.

## Are employees of different gender paid equally in all departments?

Analysen viste, at der i visse afdelinger eksisterer en lønforskel mellem kønnene, hvor mænd i gennemsnit tjener mere end kvinder i samme afdeling. Forskellene var mindre i administrative roller, men mere udtalte i salgs- og ledelsesstillinger. Lønforskelle kan forklares delvist med forskellig anciennitet og erfaring, men også mulige kønsbias i rekruttering eller forfremmelse. Det anbefales at gennemføre mere detaljerede analyser for at afdække strukturelle lønforskelle og sikre ligeløn.

## Do the family status and the distance from work influence the work-life balance?

Ja, vores data viste tydeligt, at medarbejdere med familie og især små børn oplever større udfordringer med work-life balance, især hvis de samtidig har lang pendlingstid. Kombinationen af familieforpligtelser og lange rejsetider fører ofte til lavere tilfredshed, højere stress og øget risiko for at medarbejderen overvejer jobskifte. Fleksible arbejdstider og muligheden for hjemmearbejde kunne være relevante tiltag for at støtte denne gruppe.

## Does education make people happy (satisfied from the work)?

Generelt var der en tendens til, at medarbejdere med højere uddannelse oplevede større jobtilfredshed, hvilket kan skyldes, at de oftere har job med større ansvar, bedre løn og mulighed for faglig udvikling. Dog viste analysen også, at overkvalificering i visse tilfælde kan føre til lavere tilfredshed, især hvis medarbejderen føler sig fastlåst i en stilling med lav kompleksitet eller manglende udviklingsmuligheder. Uddannelse kan altså både bidrage til tilfredshed og frustration afhængigt af jobmatch.

## Which were the challenges in the project development?

Projektet havde flere udfordringer. En stor del af dataene var ufuldstændige eller inkonsistente, hvilket krævede omfattende data cleaning og forbehandling. Derudover var der en ubalance i klassifikationsdatasættet, da langt flere medarbejdere blev i virksomheden end dem, der forlod, hvilket gjorde det nødvendigt at arbejde med metoder til håndtering af skæve klasser. En anden udfordring var at identificere meningsfulde og forklarende features, der faktisk havde predictive værdi, hvilket krævede både domæneforståelse og eksperimentering med forskellige feature engineering-teknikker.
