<h1>Create a New Blog Post</h1>
<form id="blog-form" method="post">
  {% csrf_token %}  # Add CSRF token for security
  <label for="title">Blog Post Title:</label>
  <input type="text" id="title" name="title" placeholder="Enter your blog post title" required>
  <br>
  <label for="content">Content:</label>
  <textarea id="content" name="content" rows="10" placeholder="Write your blog post content"></textarea>
  <br>
  <button type="submit">Publish Post</button>
</form>

<div id="preview"></div>

<script>
  // ... (Optional) Your existing JavaScript code for previewing title
</script>

