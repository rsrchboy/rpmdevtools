(defun fedora-new-rpm-spec-file-init ()
  (delete-region (point-min) (point-max))
  (set (make-local-variable 'indent-tabs-mode) nil)
  (set (make-local-variable 'buffer-file-coding-system) 'utf-8)
  (insert-file "/etc/fedora-rpmdevtools/spectemplate-minimal.spec")
  (setq pt (point-min))
  (when buffer-file-name
    (let ((pkgname
           (file-relative-name (file-name-sans-extension buffer-file-name))))
      (and (re-search-forward "^\\(Name:\\(\\s-+\\)\\).*$" nil t)
           (replace-match (concat (match-string 1) pkgname)))))
  (set-buffer-modified-p nil))

(remove-hook 'rpm-spec-mode-new-file-hook 'rpm-spec-initialize)
(add-hook 'rpm-spec-mode-new-file-hook 'fedora-new-rpm-spec-file-init t)
