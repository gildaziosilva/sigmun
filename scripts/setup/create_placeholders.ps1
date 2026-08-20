# Script to create placeholder files for the SIGMUN project
# Creates __init__.py for Python packages and .gitkeep for empty directories

$root = "c:\ProjetosPython\sigmun-v1\sigmun-v1"

# Module list
$modules = @(
    "sigmun_rh", "sigmun_tributos", "sigmun_contabilidade", "sigmun_compras",
    "sigmun_saude", "sigmun_educacao", "sigmun_assistencia_social", "sigmun_almoxarifado",
    "sigmun_patrimonio", "sigmun_frotas", "sigmun_obras", "sigmun_licitacoes",
    "sigmun_administracao", "sigmun_agricultura", "sigmun_controladoria", "sigmun_gabinete",
    "sigmun_ouvidoria", "sigmun_planejamento", "sigmun_procuradoria", "sigmun_transparencia",
    "sigmun_financas"
)

# Layers for each module
$layers = @(
    "domain\entities", "domain\value_objects", "domain\services", "domain\events",
    "application\commands", "application\queries", "application\use_cases",
    "infrastructure\database", "infrastructure\integrations", "infrastructure\repositories",
    "presentation\api", "presentation\schemas"
)

# Create __init__.py for core module
$corePaths = @(
    "src\core",
    "src\core\domain",
    "src\core\domain\entities",
    "src\core\domain\value_objects",
    "src\core\domain\services",
    "src\core\domain\events",
    "src\core\application",
    "src\core\application\commands",
    "src\core\application\queries",
    "src\core\application\use_cases",
    "src\core\infrastructure",
    "src\core\infrastructure\database",
    "src\core\infrastructure\integrations",
    "src\core\infrastructure\repositories",
    "src\core\presentation",
    "src\core\presentation\api",
    "src\core\presentation\schemas"
)
foreach ($p in $corePaths) {
    $initPath = Join-Path $root "$p\__init__.py"
    if (-not (Test-Path $initPath)) {
        Set-Content -Path $initPath -Value ""
    }
}

# Create __init__.py for shared module
$sharedPaths = @("src\shared", "src\shared\config", "src\shared\utils", "src\shared\exceptions", "src\shared\constants", "src\shared\security")
foreach ($p in $sharedPaths) {
    $initPath = Join-Path $root "$p\__init__.py"
    if (-not (Test-Path $initPath)) {
        Set-Content -Path $initPath -Value ""
    }
}

# Create __init__.py for modules package
$initPath = Join-Path $root "src\modules\__init__.py"
if (-not (Test-Path $initPath)) { Set-Content -Path $initPath -Value "" }

# Create __init__.py for each module and its layers
foreach ($module in $modules) {
    $modulePaths = @("src\modules\$module")
    foreach ($layer in $layers) {
        $modulePaths += "src\modules\$module\$layer"
    }
    foreach ($p in $modulePaths) {
        $initPath = Join-Path $root "$p\__init__.py"
        if (-not (Test-Path $initPath)) {
            Set-Content -Path $initPath -Value ""
        }
    }
}

# Create __init__.py for src root
$initPath = Join-Path $root "src\__init__.py"
if (-not (Test-Path $initPath)) { Set-Content -Path $initPath -Value "" }

# Create __init__.py for tests
$testPaths = @("tests", "tests\unit", "tests\integration", "tests\e2e")
foreach ($p in $testPaths) {
    $initPath = Join-Path $root "$p\__init__.py"
    if (-not (Test-Path $initPath)) {
        Set-Content -Path $initPath -Value ""
    }
}

# Create .gitkeep for non-Python directories that should be tracked
$gitkeepDirs = @(
    "frontend\admin\src",
    "frontend\admin\public",
    "frontend\portal-cidadao\src",
    "frontend\portal-cidadao\public",
    "frontend\portal-fornecedor\src",
    "frontend\portal-fornecedor\public",
    "mobile\cidadao\src",
    "mobile\fiscalizacao\src",
    "mobile\saude\src",
    "mobile\equipes-externas\src",
    "infra\docker\backend",
    "infra\docker\frontend",
    "infra\docker\database",
    "infra\terraform\modules",
    "infra\terraform\environments\dev",
    "infra\terraform\environments\homolog",
    "infra\terraform\environments\prod",
    "infra\kubernetes\base",
    "infra\kubernetes\overlays\dev",
    "infra\kubernetes\overlays\homolog",
    "infra\kubernetes\overlays\prod",
    "docs\api",
    "docs\architecture",
    "docs\diagrams"
)
foreach ($dir in $gitkeepDirs) {
    $keepPath = Join-Path $root "$dir\.gitkeep"
    if (-not (Test-Path $keepPath)) {
        Set-Content -Path $keepPath -Value ""
    }
}

Write-Host "All placeholder files created successfully."
