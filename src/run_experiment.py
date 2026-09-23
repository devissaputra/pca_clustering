from pathlib import Path
import json, matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
X,_=load_wine(return_X_y=True,as_frame=True); S=StandardScaler().fit_transform(X); pca=PCA(n_components=2).fit(S); Z=pca.transform(S); ks=range(2,7); sil=[]
for k in ks: sil.append(silhouette_score(Z,KMeans(n_clusters=k,n_init=30,random_state=42).fit_predict(Z)))
k=ks[list(sil).index(max(sil))]; labels=KMeans(n_clusters=k,n_init=30,random_state=42).fit_predict(Z); out={'best_k':int(k),'silhouette':float(max(sil)),'pc1_variance':float(pca.explained_variance_ratio_[0]),'pc2_variance':float(pca.explained_variance_ratio_[1]),'n':int(len(X))}
Path('results').mkdir(exist_ok=True); Path('results/metrics.json').write_text(json.dumps(out,indent=2))
plt.figure(figsize=(7,5)); plt.scatter(Z[:,0],Z[:,1],c=labels); plt.xlabel('PC1'); plt.ylabel('PC2'); plt.title('PCA projection and K-means clusters'); plt.tight_layout(); plt.savefig('assets/03_data_or_model.png',dpi=150); plt.close()
plt.figure(figsize=(7,5)); plt.plot(list(ks),sil,marker='o'); plt.xlabel('k'); plt.ylabel('Silhouette'); plt.title('Cluster validation'); plt.tight_layout(); plt.savefig('assets/04_evaluation_or_results.png',dpi=150); plt.close(); print(json.dumps(out,indent=2))