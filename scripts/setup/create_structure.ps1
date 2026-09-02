# Script to create the SIGMUN project directory structure
# Based on the architecture defined in SIGMUN-Docs/01-Arquitetura-Corporativa/004-Arquitetura-de-Software.md

$root = "c:\ProjetosPython\sigmun-v1\sigmun-v1"

# Module list (from 05-Modulos directory)
$modules = @(
    "sigmun_rh",
    "sigmun_tributos",
    "sigmun_contabilidade",
    "sigmun_compras",
    "sigmun_saude",
    "sigmun_educacao",
    "sigmun_assistencia_social",
    "sigmun_almoxarifado",
    "sigmun_patrimonio",
    "sigmun_frotas",
    "sigmun_obras",
    "sigmun_licitacoes",
    "sigmun_administracao",
    "sigmun_agricultura",
    "sigmun_controladoria",
    "sigmun_gabinete",
    "sigmun_ouvidoria",
    "sigmun_planejamento",
    "sigmun_procuradoria",
    "sigmun_transparencia",
    "sigmun_financas"
)

# Layer structure for each module (Clean Architecture)
$layers = @(
    "domain\entities",
    "domain\value_objects",
    "domain\services",
    "domain\events",
    "application\commands",
    "application\queries",
    "application\use_cases",
    "infrastructure\database",
    "infrastructure\integrations",
    "infrastructure\repositories",
    "presentation\api",
    "presentation\schemas"
)

# Create Core module structure
$coreLayers = $layers
foreach ($layer in $coreLayers) {
    $path = Join-Path $root "src\core\$layer"
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
    }
}

# Create Shared module structure
$sharedDirs = @("config", "utils", "exceptions", "constants", "security")
foreach ($dir in $sharedDirs) {
    $path = Join-Path $root "src\shared\$dir"
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
    }
}

# Create each business module with full Clean Architecture structure
foreach ($module in $modules) {
    foreach ($layer in $layers) {
        $path = Join-Path $root "src\modules\$module\$layer"
        if (-not (Test-Path $path)) {
            New-Item -ItemType Directory -Path $path -Force | Out-Null
        }
    }
}

# Create Frontend directories
$frontendApps = @("admin", "portal-cidadao", "portal-fornecedor")
foreach ($app in $frontendApps) {
    $path1 = Join-Path $root "frontend\$app\src"
    $path2 = Join-Path $root "frontend\$app\public"
    if (-not (Test-Path $path1)) { New-Item -ItemType Directory -Path $path1 -Force | Out-Null }
    if (-not (Test-Path $path2)) { New-Item -ItemType Directory -Path $path2 -Force | Out-Null }
}

# Create Mobile directories
$mobileApps = @("cidadao", "fiscalizacao", "saude", "equipes-externas")
foreach ($app in $mobileApps) {
    $path = Join-Path $root "mobile\$app\src"
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
    }
}

# Create Infrastructure directories
$infraDirs = @(
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
    "infra\kubernetes\overlays\prod"
)
foreach ($dir in $infraDirs) {
    $path = Join-Path $root $dir
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
    }
}

# Create Tests directories
$testDirs = @("tests\unit", "tests\integration", "tests\e2e")
foreach ($dir in $testDirs) {
    $path = Join-Path $root $dir
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
    }
}

# Create CI/CD directories
$cicdDirs = @(".github\workflows", ".github\ISSUE_TEMPLATE")
foreach ($dir in $cicdDirs) {
    $path = Join-Path $root $dir
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
    }
}

# Create Scripts directories
$scriptDirs = @("scripts\setup", "scripts\migrations", "scripts\deployment", "scripts\utilities")
foreach ($dir in $scriptDirs) {
    $path = Join-Path $root $dir
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
    }
}

# Create Docs directories
$docDirs = @("docs\api", "docs\architecture", "docs\diagrams")
foreach ($dir in $docDirs) {
    $path = Join-Path $root $dir
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
    }
}

Write-Host "All directories created successfully."
