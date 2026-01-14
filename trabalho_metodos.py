import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# ==============================================
# DADOS ORIGINAIS DO ARTIGO (Tabela 1, página 8)
# ==============================================

# Espaçamento h (definido no artigo)
h = 7.05  # metros

# Dados da Tabela 1: i, X, Y1 (superior), Y2 (inferior)
# Y1: ordenadas da margem superior da APP
# Y2: ordenadas da margem inferior da APP
x_coords = [0, 7.05, 14.1, 21.15, 28.2, 35.25, 42.3, 49.35, 56.4, 63.45,
            70.5, 77.55, 84.6, 91.65, 98.7, 105.75, 112.8, 119.85, 126.9, 133.95, 141]

y_superior = [0, 11.75, 23.5, 32.04, 32.64, 32.23, 34.07, 34.81, 36.95, 39.56,
              41.17, 38.1, 33.86, 29.62, 25.39, 21.15, 16.93, 12.69, 8.46, 4.23, 0]

y_inferior = [0, 4.24, 8.49, 12.73, 16.97, 21.22, 25.46, 27.19, 22.5, 24.9,
              23.72, 21.55, 18.35, 18.04, 18.13, 18.23, 17.12, 14.97, 10.57, 5.28, 0]

# Área a ser descontada (rua que corta o quarteirão)
area_rua = 134.4333  # m² (valor do artigo)

# Área total do quarteirão (calculada no artigo)
area_quarteirao = 10954.83  # m²

# ==============================================
# FUNÇÕES PARA CÁLCULO DE ÁREAS
# ==============================================

def regra_trapezio(y, h):
    """
    Calcula a área usando o Método dos Trapézios Composto.
    
    Parâmetros:
    y (list): Lista de ordenadas (valores de y)
    h (float): Espaçamento constante entre pontos no eixo x
    
    Retorna:
    float: Área calculada pelo método dos trapézios
    """
    n = len(y) - 1  # Número de intervalos
    soma = y[0] + y[-1]  # Primeiro e último ponto
    soma += 2 * sum(y[1:-1])  # Soma dos pontos intermediários multiplicados por 2
    
    return (h / 2) * soma

def regra_simpson(y, h):
    """
    Calcula a área usando a Primeira Regra de Simpson Composta.
    
    Parâmetros:
    y (list): Lista de ordenadas (valores de y)
    h (float): Espaçamento constante entre pontos no eixo x
    
    Retorna:
    float: Área calculada pelo método de Simpson
    """
    n = len(y) - 1
    
    # Verifica se o número de intervalos é par (requisito do método)
    if n % 2 != 0:
        raise ValueError("A Regra de Simpson exige um número par de intervalos!")
    
    soma = y[0] + y[-1]  # Primeiro e último ponto
    
    # Soma dos pontos com pesos 4 e 2 alternadamente
    for i in range(1, n):
        if i % 2 != 0:  # Índices ímpares: peso 4
            soma += 4 * y[i]
        else:  # Índices pares: peso 2
            soma += 2 * y[i]
    
    return (h / 3) * soma

# ==============================================
# CÁLCULOS COM OS MÉTODOS NUMÉRICOS
# ==============================================

print("=" * 50)
print("CÁLCULO DA ÁREA DE PRESERVAÇÃO PERMANENTE (APP)")
print("Comparação entre Métodos Numéricos")
print("=" * 50)

# 1. Cálculo pelo Método dos Trapézios
I1_trap = regra_trapezio(y_superior, h)
I2_trap = regra_trapezio(y_inferior, h)
area_total_trap = I1_trap + I2_trap
area_liquida_trap = area_total_trap - area_rua

print("\n--- MÉTODO DOS TRAPÉZIOS ---")
print(f"Área Superior (I1): {I1_trap:.4f} m²")
print(f"Área Inferior (I2): {I2_trap:.4f} m²")
print(f"Área Total Bruta:   {area_total_trap:.4f} m²")
print(f"Área Líquida (sem rua): {area_liquida_trap:.4f} m²")

# 2. Cálculo pela Primeira Regra de Simpson
I1_simp = regra_simpson(y_superior, h)
I2_simp = regra_simpson(y_inferior, h)
area_total_simp = I1_simp + I2_simp
area_liquida_simp = area_total_simp - area_rua

print("\n--- PRIMEIRA REGRA DE SIMPSON ---")
print(f"Área Superior (I1): {I1_simp:.4f} m²")
print(f"Área Inferior (I2): {I2_simp:.4f} m²")
print(f"Área Total Bruta:   {area_total_simp:.4f} m²")
print(f"Área Líquida (sem rua): {area_liquida_simp:.4f} m²")

# ==============================================
# COMPARAÇÃO COM OS RESULTADOS DO ARTIGO
# ==============================================

print("\n" + "=" * 50)
print("COMPARAÇÃO COM OS RESULTADOS DO ARTIGO")
print("=" * 50)

# Valores do artigo (Tabela 2, página 9)
area_autocad = 5777.0648  # m² (valor de referência)
area_trap_artigo = 5779.1772  # m²
area_simp_artigo = 5803.2647  # m²

print("\n--- VALORES DO ARTIGO ---")
print(f"AutoCAD (referência): {area_autocad:.4f} m²")
print(f"Trapézios (artigo):   {area_trap_artigo:.4f} m²")
print(f"Simpson (artigo):     {area_simp_artigo:.4f} m²")

print("\n--- NOSSOS CÁLCULOS ---")
print(f"Trapézios (nosso):    {area_liquida_trap:.4f} m²")
print(f"Simpson (nosso):      {area_liquida_simp:.4f} m²")

# Cálculo dos erros em relação ao AutoCAD
erro_trap_nosso = abs(area_liquida_trap - area_autocad)
erro_simp_nosso = abs(area_liquida_simp - area_autocad)
erro_trap_artigo = abs(area_trap_artigo - area_autocad)
erro_simp_artigo = abs(area_simp_artigo - area_autocad)

print("\n--- ERROS EM RELAÇÃO AO AUTOCAD ---")
print(f"Trapézios (artigo): {erro_trap_artigo:.4f} m²")
print(f"Trapézios (nosso):  {erro_trap_nosso:.4f} m²")
print(f"Simpson (artigo):   {erro_simp_artigo:.4f} m²")
print(f"Simpson (nosso):    {erro_simp_nosso:.4f} m²")

# Porcentagem do quarteirão ocupada pela APP
porcentagem_trap = (area_liquida_trap / area_quarteirao) * 100
porcentagem_simp = (area_liquida_simp / area_quarteirao) * 100

print("\n--- PORCENTAGEM DO QUARTEIRÃO OCUPADA PELA APP ---")
print(f"Área total do quarteirão: {area_quarteirao:.2f} m²")
print(f"Por Trapézios: {porcentagem_trap:.2f}%")
print(f"Por Simpson:   {porcentagem_simp:.2f}%")
print(f"No artigo:     52.75% (aprox.)")

# ==============================================
# GRÁFICOS VISUAIS
# ==============================================

# Criar figura com 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1: Área da APP
ax1.set_title('Área de Preservação Permanente (APP)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Comprimento (m)', fontsize=12)
ax1.set_ylabel('Largura (m)', fontsize=12)
ax1.grid(True, alpha=0.3)

# Plotar as duas curvas
ax1.plot(x_coords, y_superior, 'b-', linewidth=2, label='Margem Superior')
ax1.plot(x_coords, y_inferior, 'r-', linewidth=2, label='Margem Inferior')

# Preencher a área entre as curvas
ax1.fill_between(x_coords, y_inferior, y_superior, alpha=0.3, color='green', label='APP')

# Adicionar pontos de medição
ax1.scatter(x_coords, y_superior, color='blue', s=50, zorder=5, label='Pontos Superior')
ax1.scatter(x_coords, y_inferior, color='red', s=50, zorder=5, label='Pontos Inferior')

ax1.legend(fontsize=10, loc='upper right')
ax1.set_xlim(0, 141)
ax1.set_ylim(0, max(y_superior) + 5)

# Gráfico 2: Comparação dos métodos
metodos = ['AutoCAD', 'Trapézios\n(Nosso)', 'Simpson\n(Nosso)']
areas = [area_autocad, area_liquida_trap, area_liquida_simp]
cores = ['gray', 'blue', 'red']

ax2.set_title('Comparação das Áreas Calculadas', fontsize=14, fontweight='bold')
ax2.set_ylabel('Área (m²)', fontsize=12)
ax2.set_xlabel('Método de Cálculo', fontsize=12)

bars = ax2.bar(metodos, areas, color=cores, alpha=0.7, edgecolor='black')
ax2.grid(True, alpha=0.3, axis='y')

# Adicionar valores nas barras
for bar, area in zip(bars, areas):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 10,
             f'{area:.1f} m²', ha='center', va='bottom', fontsize=11, fontweight='bold')

# Linha de referência do AutoCAD
ax2.axhline(y=area_autocad, color='gray', linestyle='--', alpha=0.7, linewidth=1, label='Referência AutoCAD')

# Calcular e mostrar os erros
erros_texto = f'Erros em relação ao AutoCAD:\n' \
              f'Trapézios: {erro_trap_nosso:.2f} m²\n' \
              f'Simpson: {erro_simp_nosso:.2f} m²'

ax2.text(0.02, 0.98, erros_texto, transform=ax2.transAxes,
         fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

ax2.legend(fontsize=10)

plt.tight_layout()
plt.show()

# ==============================================
# GRÁFICO ADICIONAL: VISUALIZAÇÃO DA APROXIMAÇÃO
# ==============================================

fig2, (ax3, ax4) = plt.subplots(2, 1, figsize=(12, 10))

# Subplot 1: Aproximação por Trapézios
ax3.set_title('Aproximação pelo Método dos Trapézios', fontsize=14, fontweight='bold')
ax3.set_ylabel('Largura (m)', fontsize=12)
ax3.grid(True, alpha=0.3)

# Plotar a curva original
ax3.plot(x_coords, y_superior, 'b-', linewidth=2, alpha=0.5, label='Curva Original Superior')
ax3.plot(x_coords, y_inferior, 'r-', linewidth=2, alpha=0.5, label='Curva Original Inferior')

# Preencher com trapézios (aproximação)
for i in range(len(x_coords)-1):
    # Trapézio superior
    verts_sup = [(x_coords[i], 0), 
                 (x_coords[i], y_superior[i]),
                 (x_coords[i+1], y_superior[i+1]),
                 (x_coords[i+1], 0)]
    poly_sup = Polygon(verts_sup, alpha=0.2, color='blue', label='Trapézio Superior' if i==0 else "")
    ax3.add_patch(poly_sup)
    
    # Trapézio inferior (considerando eixo x como referência)
    verts_inf = [(x_coords[i], 0),
                 (x_coords[i], -y_inferior[i]),
                 (x_coords[i+1], -y_inferior[i+1]),
                 (x_coords[i+1], 0)]
    poly_inf = Polygon(verts_inf, alpha=0.2, color='red', label='Trapézio Inferior' if i==0 else "")
    ax3.add_patch(poly_inf)

ax3.set_xlim(0, 141)
ax3.set_ylim(-max(y_inferior)-5, max(y_superior)+5)
ax3.axhline(y=0, color='black', linewidth=0.5)
ax3.set_xlabel('Comprimento (m)', fontsize=12)
ax3.legend(fontsize=10, loc='upper right')

# Subplot 2: Aproximação por Simpson (parábolas)
ax4.set_title('Aproximação pela Regra de Simpson (Parábolas)', fontsize=14, fontweight='bold')
ax4.set_xlabel('Comprimento (m)', fontsize=12)
ax4.set_ylabel('Largura (m)', fontsize=12)
ax4.grid(True, alpha=0.3)

# Plotar a curva original
ax4.plot(x_coords, y_superior, 'b-', linewidth=2, alpha=0.5, label='Curva Original Superior')
ax4.plot(x_coords, y_inferior, 'r-', linewidth=2, alpha=0.5, label='Curva Original Inferior')

# Desenhar parábolas aproximadas (a cada 2 intervalos)
for i in range(0, len(x_coords)-2, 2):
    # Pontos para a parábola
    x_parabola = [x_coords[i], x_coords[i+1], x_coords[i+2]]
    y_parabola_sup = [y_superior[i], y_superior[i+1], y_superior[i+2]]
    y_parabola_inf = [y_inferior[i], y_inferior[i+1], y_inferior[i+2]]
    
    # Gerar mais pontos para uma curva suave
    x_fine = np.linspace(x_coords[i], x_coords[i+2], 50)
    
    # Interpolação quadrática
    # Coeficientes da parábola para a margem superior
    coeff_sup = np.polyfit(x_parabola, y_parabola_sup, 2)
    y_fine_sup = np.polyval(coeff_sup, x_fine)
    
    # Coeficientes da parábola para a margem inferior
    coeff_inf = np.polyfit(x_parabola, y_parabola_inf, 2)
    y_fine_inf = np.polyval(coeff_inf, x_fine)
    
    # Preencher a área entre as parábolas
    ax4.fill_between(x_fine, y_fine_inf, y_fine_sup, alpha=0.2, color='green', label='Área Simpson' if i==0 else "")

# Adicionar pontos de amostragem
ax4.scatter(x_coords, y_superior, color='blue', s=30, zorder=5, alpha=0.7, label='Pontos Superior')
ax4.scatter(x_coords, y_inferior, color='red', s=30, zorder=5, alpha=0.7, label='Pontos Inferior')

ax4.set_xlim(0, 141)
ax4.set_ylim(0, max(y_superior)+5)
ax4.legend(fontsize=10, loc='upper right')

plt.tight_layout()
plt.show()

# ==============================================
# GRÁFICO 3: COMPARAÇÃO DE ERROS
# ==============================================

fig3, ax5 = plt.subplots(figsize=(10, 6))

metodos_erro = ['Trapézios\n(Artigo)', 'Trapézios\n(Nosso)', 'Simpson\n(Artigo)', 'Simpson\n(Nosso)']
erros = [erro_trap_artigo, erro_trap_nosso, erro_simp_artigo, erro_simp_nosso]
cores_erro = ['lightblue', 'blue', 'lightcoral', 'red']

ax5.set_title('Erros em Relação à Referência AutoCAD', fontsize=14, fontweight='bold')
ax5.set_ylabel('Erro Absoluto (m²)', fontsize=12)
ax5.set_xlabel('Método de Cálculo', fontsize=12)

bars_erro = ax5.bar(metodos_erro, erros, color=cores_erro, alpha=0.8, edgecolor='black')
ax5.grid(True, alpha=0.3, axis='y')

# Adicionar valores nas barras
for bar, erro in zip(bars_erro, erros):
    height = bar.get_height()
    ax5.text(bar.get_x() + bar.get_width()/2., height + 0.2,
             f'{erro:.2f} m²', ha='center', va='bottom', fontsize=11)

# Linha horizontal em y=0
ax5.axhline(y=0, color='black', linewidth=0.5)

# Adicionar porcentagem de erro
porcentagens_erro = [(erro/area_autocad)*100 for erro in erros]
for i, (bar, porcentagem) in enumerate(zip(bars_erro, porcentagens_erro)):
    ax5.text(bar.get_x() + bar.get_width()/2., bar.get_height()/2,
             f'({porcentagem:.3f}%)', ha='center', va='center', 
             color='white', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()

# ==============================================
# RESUMO FINAL
# ==============================================

print("\n" + "=" * 50)
print("RESUMO DA ANÁLISE")
print("=" * 50)

print(f"\n1. DADOS UTILIZADOS:")
print(f"   • Pontos de medição: {len(x_coords)} pontos")
print(f"   • Espaçamento (h): {h} metros")
print(f"   • Comprimento total: {x_coords[-1]} metros")

print(f"\n2. RESULTADOS OBTIDOS:")
print(f"   • Método dos Trapézios: {area_liquida_trap:.2f} m²")
print(f"   • Regra de Simpson:     {area_liquida_simp:.2f} m²")

print(f"\n3. COMPARAÇÃO COM O ARTIGO:")
print(f"   • AutoCAD (referência): {area_autocad:.2f} m²")
print(f"   • Diferença Trapézios:  {area_liquida_trap - area_autocad:+.2f} m²")
print(f"   • Diferença Simpson:    {area_liquida_simp - area_autocad:+.2f} m²")

print(f"\n4. IMPACTO NO QUARTEIRÃO:")
print(f"   • Área total: {area_quarteirao:.2f} m²")
print(f"   • APP por Trapézios: {porcentagem_trap:.2f}%")
print(f"   • APP por Simpson:   {porcentagem_simp:.2f}%")
print(f"   • Conclusão: Mais da metade do terreno está comprometido")

print(f"\n5. CONCLUSÃO DO ARTIGO (validada):")
print(f"   • O Método dos Trapézios apresentou menor erro")
print(f"   • Isso se deve ao comportamento quase linear do córrego")
print(f"   • Cerca de 52.75% do quarteirão é APP (não edificável)")
