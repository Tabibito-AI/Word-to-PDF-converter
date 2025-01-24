# Gemini Paper Summarizer (Word to PDF Converter)

## 概要

Gemini APIを使用して学術論文の要約を生成するコマンドラインツールです。

注: 中国語、英語、フランス語、ドイツ語、日本語、韓国語、スペイン語を含む多言語をサポートしています。

## 例

[examples](examples) ディレクトリに、以下の要約を含むサンプル出力があります。

- [Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., … Polosukhin, I. (2017). Attention Is All You Need.](https://arxiv.org/abs/1706.03762v7)

### その他の日本語の要約

- [(2018) What you can cram into a single vector: Probing sentence embeddings for linguistic properties](https://7shi.hateblo.jp/entry/2025/01/09/032708)
- [(2018) Improving language understanding by generative pre-training](https://7shi.hateblo.jp/entry/2025/01/08/023518)
- [(2018) BERT: Pre-training of deep bidirectional Transformers for language understanding](https://7shi.hateblo.jp/entry/2025/01/09/011331)
- [(2019) BERT rediscovers the classical NLP pipeline](https://7shi.hateblo.jp/entry/2025/01/09/014758)
- [(2019) Linguistic knowledge and transferability of contextual representations](https://7shi.hateblo.jp/entry/2025/01/09/024710)
- [(2019) A Structural Probe for Finding Syntax in Word Representations](https://7shi.hateblo.jp/entry/2025/01/09/030338)
- [(2019) What does BERT look at? An analysis of BERT’s attention](https://7shi.hateblo.jp/entry/2025/01/09/034240)
- [(2023) Text Embeddings Reveal (Almost) As Much As Text](https://7shi.hateblo.jp/entry/2025/01/05/203512)
- [(2024) Large Concept Models: Language Modeling in a Sentence Representation Space](https://7shi.hateblo.jp/entry/2025/01/04/232224)

DeepSeek

- [(2024) DeepSeek LLM: Scaling open-source language models with longtermism.](https://7shi.hateblo.jp/entry/2025/01/07/225023)
- [(2024) DeepSeek-V2: A strong, economical, and efficient Mixture-of-Experts language model.](https://7shi.hateblo.jp/entry/2025/01/07/234352)
- [(2024) DeepSeek-Coder-V2: Breaking the barrier of closed-source models in code intelligence.](https://7shi.hateblo.jp/entry/2025/01/07/235825)
- [(2024) DeepSeek-V3 Technical Report](https://7shi.hateblo.jp/entry/2025/01/08/000133)

## 前提条件

- Python 3.10+
- Gemini APIキー ([Google AI Studio](https://aistudio.google.com/) から取得)

注: ローカル環境のセットアップが難しい場合は、@shoei05 による以下の Google Colab Notebook (日本語で解説) を参照してください。

- [論文要約 gemini-paper-summarizer を Google Colab で使用する](https://colab.research.google.com/drive/1yj02UYLNjXvz4nInB5zGzvrcawaJ_Mua?usp=sharing)

## インストール

1. リポジトリをクローンします
2. 依存関係をインストールします:
   ```
   uv sync
   ```
3. プロジェクトディレクトリに `.env` ファイルを作成し、Gemini APIキーを設定します:
   ```bash
   GEMINI_API_KEY=your_api_key_here
   ```
4. `uv run gp-summarize /Users/masuda_1/Desktop/letter.pdf` を実行します
   ```
5. 英文論文を日本語に翻訳してまとめる機能を実行するには、以下のコマンドを実行します。
Run `uv run gp-summarize -l ja /Users/masuda_1/Desktop/letter.pdf`
   ```

## 使用方法

```bash
uv run gp-summarize path/to/paper.pdf
```

ツールは、異なる種類の要約を含む複数のmarkdownファイルを生成します。

1.  アブストラクトの翻訳
2.  論文全体の要約
3.  論文の章とセクションのJSON構造
4.  各主要セクションの個別の要約 (翻訳ではない)
5.  上記の1〜4を1つのファイルにまとめたもの

出力ファイルは、入力PDFファイル名に基づいて命名されます。上記の1〜4のファイルはディレクトリに保存され、連続番号が付けられます (例: `paper/001.md`、`paper/002.md`など)。結合されたファイルは `paper.md` という名前になります。

注: プロセスが中断された場合 (Ctrl+C または 429 レート制限エラーなど)、既存の出力ファイルはスキップされるため、プロセスをスムーズに再実行できます。

### 出力形式

各プロンプトに対して、ツールは以下の内容を含むmarkdownファイルを生成します。

- タイトル (プロンプト番号)
- トークンに関する統計情報
- プロンプト
- AIによって生成された応答

セクション構造は、JSON形式と階層リストの両方で表示されます。

## コマンドラインオプション

```
python -m gp_summarize [-h] [-d OUTPUT_DIR] [-o OUTPUT] [-l {de,en,es,fr,ja,ko,zh}] [--version] pdf_paths [pdf_paths ...]
```

- `pdf_paths`: **必須** 要約する1つ以上のPDFファイルへのパス
    - 複数のPDFファイルを指定できます
    - Windowsではワイルドカード (`*`) がサポートされています

- `-d, --output-dir`: オプション。中間ファイルの出力ディレクトリを指定します
    - 複数のPDFファイルを処理する場合に推奨されます

- `-o, --output`: オプション。要約の出力ファイルを指定します
    - 単一のPDFファイルでのみ使用できます

- `-l, --language`: オプション。出力言語を指定します
    - サポートされている言語: `de` (ドイツ語), `en` (英語), `es` (スペイン語), `fr` (フランス語), `ja` (日本語), `ko` (韓国語), `zh` (中国語)
    - デフォルト: システム言語設定に基づく

- `--version`: バージョン情報を表示します

### 例

単一のPDFを要約する:
```
python -m gp_summarize paper.pdf
```

複数のPDFを要約する:
```
python -m gp_summarize paper1.pdf paper2.pdf
```

出力ディレクトリを指定する:
```
python -m gp_summarize -d ./outputs paper.pdf
```

特定の言語で要約する:
```
python -m gp_summarize -l ja paper.pdf
```

## ライセンス

CC0 1.0 Universal
